import React, { useState } from 'react';
import api from '../services/api';

export default function RecommendationPage() {
  const [result, setResult] = useState(null);

  const fetchRec = async () => {
    const { data } = await api.get('/career-recommendation');
    setResult(data);
  };

  return (
    <section className="card">
      <h2>Career Recommendation</h2>
      <button onClick={fetchRec}>Generate Recommendation</button>
      {result && (
        <div>
          <h3>{result.recommended_career.name}</h3>
          <p>Suitability: {result.suitability_score}%</p>
          <p>Required Skills: {result.recommended_career.required_skills.join(', ')}</p>
        </div>
      )}
    </section>
  );
}
