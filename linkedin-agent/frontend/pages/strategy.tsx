import { useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

export default function Strategy() {
  const [pillars, setPillars] = useState<string[]>([]);
  const [calendar, setCalendar] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  async function generate() {
    setLoading(true);
    const res = await fetch(`${API_BASE}/content/strategy`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ interests: ['AI', 'Leadership', 'Product'], frequency_per_week: 3 }),
    });
    const data = await res.json();
    setPillars(data.pillars || []);
    setCalendar(data.calendar || []);
    setLoading(false);
  }

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Content Strategy</h2>
      <button onClick={generate} disabled={loading} style={{ padding: 8, border: '1px solid #ccc' }}>
        {loading ? 'Generating...' : 'Generate Strategy'}
      </button>
      <section>
        <h3>Pillars</h3>
        <ul>{pillars.map((p, i) => <li key={i}>{p}</li>)}</ul>
      </section>
      <section>
        <h3>Calendar</h3>
        <ul>
          {calendar.map((c, i) => (
            <li key={i}>{new Date(c.date).toLocaleDateString()} — {c.post_type} — {c.topic}</li>
          ))}
        </ul>
      </section>
    </main>
  );
}