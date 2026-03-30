import React, { useState } from 'react';
import api from '../services/api';

export default function RegisterPage() {
  const [form, setForm] = useState({ username: '', email: '', password: '', first_name: '', last_name: '' });
  const [message, setMessage] = useState('');

  const submit = async (e) => {
    e.preventDefault();
    const { data } = await api.post('/register', form);
    localStorage.setItem('token', data.token);
    setMessage('Registered successfully.');
  };

  return (
    <form className="card form" onSubmit={submit}>
      <h2>Register</h2>
      {Object.keys(form).map((key) => (
        <input key={key} placeholder={key} type={key === 'password' ? 'password' : 'text'} value={form[key]} onChange={(e) => setForm({ ...form, [key]: e.target.value })} required />
      ))}
      <button type="submit">Create account</button>
      <p>{message}</p>
    </form>
  );
}
