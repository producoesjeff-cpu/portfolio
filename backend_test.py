#!/usr/bin/env python3
"""
Backend Test Suite for Gaffer Portfolio - Jeferson Rodrigues
Tests all backend endpoints and functionality
"""

import requests
import json
import os
from datetime import datetime
from typing import Dict, Any

# Get backend URL from environment
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://film-creator-4.preview.emergentagent.com')

class GafferPortfolioTester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.api_url = f"{self.base_url}/api"
        self.session = requests.Session()
        self.test_results = []
        self.admin_token = None
        
    def log_test(self, test_name: str, success: bool, details: str = "", response_data: Any = None):
        """Log test results"""
        result = {
            "test": test_name,
            "success": success,
            "details": details,
            "timestamp": datetime.now().isoformat(),
            "response_data": response_data
        }
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}")
        if details:
            print(f"   Details: {details}")
        if not success and response_data:
            print(f"   Response: {response_data}")
        print()

    def test_health_endpoint(self):
        """Test GET /health endpoint"""
        try:
            # Test on backend port directly since external routing may go to frontend
            response = self.session.get("http://localhost:8001/health", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                expected_keys = ["status", "database", "email_configured", "cloudinary"]
                
                if all(key in data for key in expected_keys):
                    self.log_test(
                        "Health Check Endpoint", 
                        True, 
                        f"Status: {data.get('status')}, DB: {data.get('database')}, Email: {data.get('email_configured')}"
                    )
                    return True
                else:
                    self.log_test(
                        "Health Check Endpoint", 
                        False, 
                        f"Missing expected keys. Got: {list(data.keys())}", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Health Check Endpoint", 
                    False, 
                    f"HTTP {response.status_code}", 
                    response.text
                )
                return False
                
        except Exception as e:
            self.log_test("Health Check Endpoint", False, f"Exception: {str(e)}")
            return False

    def test_portfolio_endpoint(self):
        """Test GET /api/portfolio endpoint"""
        try:
            response = self.session.get(f"{self.api_url}/portfolio", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check required structure
                expected_sections = ["personal", "demoReel", "services", "featuredWorks", "recentProjects", "clients"]
                missing_sections = [section for section in expected_sections if section not in data]
                
                if missing_sections:
                    self.log_test(
                        "Portfolio Structure", 
                        False, 
                        f"Missing sections: {missing_sections}", 
                        data
                    )
                    return False
                
                # Validate personal info
                personal = data.get("personal", {})
                if personal.get("name") == "Jeferson Rodrigues" and "Gaffer" in personal.get("role", ""):
                    self.log_test(
                        "Portfolio Personal Info", 
                        True, 
                        f"Name: {personal.get('name')}, Role: {personal.get('role')}"
                    )
                else:
                    self.log_test(
                        "Portfolio Personal Info", 
                        False, 
                        f"Incorrect personal info. Name: {personal.get('name')}, Role: {personal.get('role')}"
                    )
                
                # Check services
                services = data.get("services", [])
                if len(services) > 0:
                    self.log_test(
                        "Portfolio Services", 
                        True, 
                        f"Found {len(services)} services"
                    )
                else:
                    self.log_test(
                        "Portfolio Services", 
                        False, 
                        "No services found"
                    )
                
                # Check clients (should include Netflix, MIO, Seara, etc.)
                clients = data.get("clients", [])
                client_names = [client.get("name", "").lower() for client in clients]
                expected_clients = ["netflix", "mio", "seara"]
                found_clients = [client for client in expected_clients if any(client in name for name in client_names)]
                
                if len(found_clients) > 0:
                    self.log_test(
                        "Portfolio Clients", 
                        True, 
                        f"Found expected clients: {found_clients}"
                    )
                else:
                    self.log_test(
                        "Portfolio Clients", 
                        False, 
                        f"Expected clients not found. Available: {client_names}"
                    )
                
                self.log_test(
                    "Portfolio Endpoint", 
                    True, 
                    f"Successfully retrieved portfolio data with all sections"
                )
                return True
                
            else:
                self.log_test(
                    "Portfolio Endpoint", 
                    False, 
                    f"HTTP {response.status_code}", 
                    response.text
                )
                return False
                
        except Exception as e:
            self.log_test("Portfolio Endpoint", False, f"Exception: {str(e)}")
            return False

    def test_contact_endpoint(self):
        """Test POST /api/contact endpoint"""
        try:
            # Test valid contact message
            contact_data = {
                "name": "Maria Silva",
                "email": "maria.silva@exemplo.com",
                "phone": "+55 11 98765-4321",
                "subject": "Orçamento para Produção",
                "message": "Olá Jeferson, gostaria de solicitar um orçamento para iluminação de uma produção comercial. Podemos conversar?"
            }
            
            response = self.session.post(
                f"{self.api_url}/contact", 
                json=contact_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data.get("success") and "mensagem enviada" in data.get("message", "").lower():
                    self.log_test(
                        "Contact Form Submission", 
                        True, 
                        f"Message sent successfully: {data.get('message')}"
                    )
                else:
                    self.log_test(
                        "Contact Form Submission", 
                        False, 
                        f"Unexpected response format", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Contact Form Submission", 
                    False, 
                    f"HTTP {response.status_code}", 
                    response.text
                )
                return False
            
            # Test validation - invalid email
            invalid_data = {
                "name": "Test User",
                "email": "invalid-email",
                "subject": "Test",
                "message": "Test message"
            }
            
            response = self.session.post(
                f"{self.api_url}/contact", 
                json=invalid_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 422:  # Validation error expected
                self.log_test(
                    "Contact Form Validation", 
                    True, 
                    "Correctly rejected invalid email format"
                )
            else:
                self.log_test(
                    "Contact Form Validation", 
                    False, 
                    f"Should have rejected invalid email. Got HTTP {response.status_code}"
                )
            
            # Test missing required fields
            incomplete_data = {
                "name": "Test User"
                # Missing email, subject, message
            }
            
            response = self.session.post(
                f"{self.api_url}/contact", 
                json=incomplete_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 422:  # Validation error expected
                self.log_test(
                    "Contact Form Required Fields", 
                    True, 
                    "Correctly rejected incomplete data"
                )
            else:
                self.log_test(
                    "Contact Form Required Fields", 
                    False, 
                    f"Should have rejected incomplete data. Got HTTP {response.status_code}"
                )
            
            return True
            
        except Exception as e:
            self.log_test("Contact Endpoint", False, f"Exception: {str(e)}")
            return False

    def test_admin_login(self):
        """Test admin login endpoint"""
        try:
            login_data = {
                "username": "admin",
                "password": "admin123"
            }
            
            response = self.session.post(
                f"{self.api_url}/admin/login",
                json=login_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if "access_token" in data and "token_type" in data:
                    self.admin_token = data["access_token"]
                    self.log_test(
                        "Admin Login", 
                        True, 
                        f"Successfully logged in as admin"
                    )
                    return True
                else:
                    self.log_test(
                        "Admin Login", 
                        False, 
                        "Missing token in response", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "Admin Login", 
                    False, 
                    f"HTTP {response.status_code}", 
                    response.text
                )
                return False
                
        except Exception as e:
            self.log_test("Admin Login", False, f"Exception: {str(e)}")
            return False

    def test_admin_endpoints(self):
        """Test admin-protected endpoints"""
        if not self.admin_token:
            self.log_test("Admin Endpoints", False, "No admin token available")
            return False
        
        headers = {
            "Authorization": f"Bearer {self.admin_token}",
            "Content-Type": "application/json"
        }
        
        try:
            # Test admin portfolio endpoint
            response = self.session.get(f"{self.api_url}/admin/portfolio", headers=headers, timeout=10)
            
            if response.status_code == 200:
                self.log_test(
                    "Admin Portfolio Access", 
                    True, 
                    "Successfully accessed admin portfolio"
                )
            else:
                self.log_test(
                    "Admin Portfolio Access", 
                    False, 
                    f"HTTP {response.status_code}"
                )
            
            # Test admin projects endpoint
            response = self.session.get(f"{self.api_url}/admin/projects", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.log_test(
                    "Admin Projects Access", 
                    True, 
                    f"Successfully accessed projects list ({len(data)} projects)"
                )
            else:
                self.log_test(
                    "Admin Projects Access", 
                    False, 
                    f"HTTP {response.status_code}"
                )
            
            # Test admin clients endpoint
            response = self.session.get(f"{self.api_url}/admin/clients", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.log_test(
                    "Admin Clients Access", 
                    True, 
                    f"Successfully accessed clients list ({len(data)} clients)"
                )
            else:
                self.log_test(
                    "Admin Clients Access", 
                    False, 
                    f"HTTP {response.status_code}"
                )
            
            # Test admin messages endpoint
            response = self.session.get(f"{self.api_url}/admin/messages", headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.log_test(
                    "Admin Messages Access", 
                    True, 
                    f"Successfully accessed messages ({data.get('total', 0)} total)"
                )
            else:
                self.log_test(
                    "Admin Messages Access", 
                    False, 
                    f"HTTP {response.status_code}"
                )
            
            return True
            
        except Exception as e:
            self.log_test("Admin Endpoints", False, f"Exception: {str(e)}")
            return False

    def test_api_status(self):
        """Test API status endpoint"""
        try:
            response = self.session.get(f"{self.api_url}/", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if "Gaffer Portfolio API" in data.get("message", ""):
                    self.log_test(
                        "API Status", 
                        True, 
                        f"API is online: {data.get('message')}"
                    )
                    return True
                else:
                    self.log_test(
                        "API Status", 
                        False, 
                        "Unexpected API message", 
                        data
                    )
                    return False
            else:
                self.log_test(
                    "API Status", 
                    False, 
                    f"HTTP {response.status_code}", 
                    response.text
                )
                return False
                
        except Exception as e:
            self.log_test("API Status", False, f"Exception: {str(e)}")
            return False

    def run_all_tests(self):
        """Run all backend tests"""
        print(f"🚀 Starting Gaffer Portfolio Backend Tests")
        print(f"Backend URL: {self.base_url}")
        print(f"API URL: {self.api_url}")
        print("=" * 60)
        
        # Core functionality tests
        self.test_health_endpoint()
        self.test_api_status()
        self.test_portfolio_endpoint()
        self.test_contact_endpoint()
        
        # Admin functionality tests
        if self.test_admin_login():
            self.test_admin_endpoints()
        
        # Summary
        print("=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result["success"])
        total = len(self.test_results)
        
        print(f"Total Tests: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {total - passed}")
        print(f"Success Rate: {(passed/total)*100:.1f}%")
        
        if total - passed > 0:
            print("\n❌ FAILED TESTS:")
            for result in self.test_results:
                if not result["success"]:
                    print(f"  - {result['test']}: {result['details']}")
        
        print("\n" + "=" * 60)
        return passed == total

if __name__ == "__main__":
    tester = GafferPortfolioTester()
    success = tester.run_all_tests()
    
    if success:
        print("🎉 All tests passed!")
        exit(0)
    else:
        print("💥 Some tests failed!")
        exit(1)