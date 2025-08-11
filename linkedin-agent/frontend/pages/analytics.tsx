import { useEffect, useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

type Summary = { total_posts: number; total_impressions: number; total_likes: number; total_comments: number; total_shares: number };

type Row = { post_id: number; impressions: number; likes: number; comments: number; shares: number; created_at: string };

export default function Analytics() {
  const [summary, setSummary] = useState<Summary | null>(null);
  const [rows, setRows] = useState<Row[]>([]);

  useEffect(() => {
    fetch(`${API_BASE}/analytics/summary`).then(r => r.json()).then(setSummary);
    fetch(`${API_BASE}/analytics/posts`).then(r => r.json()).then(setRows);
  }, []);

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Analytics</h2>
      {summary && (
        <div>
          <div>Posts: {summary.total_posts}</div>
          <div>Impressions: {summary.total_impressions}</div>
          <div>Likes: {summary.total_likes}</div>
          <div>Comments: {summary.total_comments}</div>
          <div>Shares: {summary.total_shares}</div>
        </div>
      )}
      <h3>Recent Metrics</h3>
      <ul>
        {rows.map(r => (
          <li key={`${r.post_id}-${r.created_at}`}>Post #{r.post_id} — {r.impressions} imp / {r.likes} 👍 / {r.comments} 💬 / {r.shares} 🔁</li>
        ))}
      </ul>
    </main>
  );
}