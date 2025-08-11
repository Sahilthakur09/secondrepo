import { useEffect, useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

type Item = { id: number; content: string; post_type: string; status: string; scheduled_at?: string };

export default function CalendarPage() {
  const [items, setItems] = useState<Item[]>([]);

  useEffect(() => {
    fetch(`${API_BASE}/content/calendar`).then(r => r.json()).then(setItems);
  }, []);

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Scheduled Posts</h2>
      <ul>
        {items.map(i => (
          <li key={i.id}>
            #{i.id} — {i.post_type} — {i.status} — {i.scheduled_at ? new Date(i.scheduled_at).toLocaleString() : 'n/a'}
          </li>
        ))}
      </ul>
    </main>
  );
}