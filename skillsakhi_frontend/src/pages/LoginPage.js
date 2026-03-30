import React, { useState } from 'react';
import api from '../services/api';

export default function LoginPage() {
  const [form, setForm] = useState({ username: '', password: '' });
  const [message, setMessage] = useState('');

  const submit = async (e) => {
    e.preventDefault();
    const { data } = await api.post('/login', form);
    localStorage.setItem('token', data.token);
    setMessage('Logged in successfully.');
  };

  return (
    <form className="card form" onSubmit={submit}>
      <h2>Login</h2>
      <input placeholder="username" value={form.username} onChange={(e) => setForm({ ...form, username: e.target.value })} required />
      <input placeholder="password" type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} required />
      <button type="submit">Login</button>
      <p>{message}</p>
    </form>
  );
}
