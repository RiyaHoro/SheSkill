import React from 'react';
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';

const SkillGapChart = ({ requiredCount, haveCount, gapCount }) => {
  const data = [
    { name: 'Required', value: requiredCount },
    { name: 'Current', value: haveCount },
    { name: 'Gap', value: gapCount },
  ];

  return (
    <div className="card chart-card">
      <h3>Skill Gap Overview</h3>
      <ResponsiveContainer width="100%" height={280}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" fill="#7c3aed" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default SkillGapChart;
