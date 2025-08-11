import { useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

export default function Compose() {
  const [postType, setPostType] = useState('text');
  const [prompt, setPrompt] = useState('Share three insights about leading AI adoption.');
  const [content, setContent] = useState('');
  const [hashtags, setHashtags] = useState<string[]>([]);
  const [scheduledAt, setScheduledAt] = useState('');

  async function generate() {
    const res = await fetch(`${API_BASE}/content/generate`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ post_type: postType, prompt })
    });
    const data = await res.json();
    setContent(data.content);
    setHashtags(data.hashtags || []);
  }

  async function optimize() {
    const res = await fetch(`${API_BASE}/content/optimize`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content })
    });
    const data = await res.json();
    setContent(data.content);
    setHashtags(data.hashtags || []);
  }

  async function schedule() {
    const res = await fetch(`${API_BASE}/content/schedule`, {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ content, post_type: postType, scheduled_at: scheduledAt })
    });
    const data = await res.json();
    alert(`Scheduled post #${data.id} at ${data.scheduled_at}`);
  }

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Compose</h2>
      <div>
        <label>Type: </label>
        <select value={postType} onChange={e => setPostType(e.target.value)}>
          <option value="text">Text</option>
          <option value="carousel">Carousel</option>
          <option value="article">Article</option>
          <option value="poll">Poll</option>
        </select>
      </div>
      <div>
        <textarea value={prompt} onChange={e => setPrompt(e.target.value)} rows={3} style={{ width: '100%', marginTop: 8 }} />
      </div>
      <button onClick={generate} style={{ marginTop: 8 }}>Generate</button>
      <div>
        <textarea value={content} onChange={e => setContent(e.target.value)} rows={12} style={{ width: '100%', marginTop: 12 }} />
      </div>
      <div>Hashtags: {hashtags.join(' ')}</div>
      <button onClick={optimize} style={{ marginTop: 8 }}>Optimize</button>
      <div style={{ marginTop: 12 }}>
        <label>Schedule at (UTC): </label>
        <input type="datetime-local" value={scheduledAt} onChange={e => setScheduledAt(e.target.value)} />
        <button onClick={schedule} style={{ marginLeft: 8 }}>Schedule</button>
      </div>
    </main>
  );
}