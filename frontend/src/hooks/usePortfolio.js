import { useState, useEffect } from 'react';
import { fetchPortfolioData } from '../data/mock';

export const usePortfolio = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const portfolioData = await fetchPortfolioData();
      setData(portfolioData);
      setError(null);
    } catch (err) {
      setError(err.message);
      console.error('Erro ao carregar portfólio:', err);
    } finally {
      setLoading(false);
    }
  };

  const refetch = async () => {
    await loadData();
  };

  return { data, loading, error, refetch };
};