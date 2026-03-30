import React, { useState } from 'react';
import api from '../services/api';

export default function ProfilePage() {
  const [form, setForm] = useState({ age: '', education_level: '', location: '', interests: '', existing_skills: '', work_preference: 'full_time' });
  const [message, setMessage] = useState('');

  const submit = async (e) => {
    e.preventDefault();
    const payload = { ...form, existing_skills: form.existing_skills.split(',').map((s) => s.trim()) };
    await api.post('/profile', payload);
    setMessage('Profile saved successfully.');
  };

  return (
    <form className="card form" onSubmit={submit}>
      <h2>Profile</h2>
      <input type="number" placeholder="Age" value={form.age} onChange={(e) => setForm({ ...form, age: e.target.value })} required />
      <input placeholder="Education level" value={form.education_level} onChange={(e) => setForm({ ...form, education_level: e.target.value })} required />
      <input placeholder="Location" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} required />
      <input placeholder="Interests (comma separated)" value={form.interests} onChange={(e) => setForm({ ...form, interests: e.target.value })} required />
      <input placeholder="Existing skills (comma separated)" value={form.existing_skills} onChange={(e) => setForm({ ...form, existing_skills: e.target.value })} required />
      <select value={form.work_preference} onChange={(e) => setForm({ ...form, work_preference: e.target.value })}>
        <option value="full_time">Full time</option>
        <option value="part_time">Part time</option>
        <option value="wfh">Work from home</option>
        <option value="freelancing">Freelancing</option>
      </select>
      <button type="submit">Save Profile</button>
      <p>{message}</p>
    </form>
  );
}
