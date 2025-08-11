import Link from 'next/link';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

export default function Home() {
  const loginUrl = `${API_BASE}/auth/linkedin/login`;
  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h1>LinkedIn Personal Branding AI Agent</h1>
      <p>Manage your brand: analyze, plan, create, schedule, and track.</p>
      <div style={{ marginTop: 16 }}>
        <a href={loginUrl} style={{ padding: 10, background: '#0a66c2', color: 'white', borderRadius: 6 }}>Connect LinkedIn</a>
      </div>
      <nav style={{ display: 'flex', gap: 12, marginTop: 20 }}>
        <Link href="/strategy">Strategy</Link>
        <Link href="/compose">Compose</Link>
        <Link href="/calendar">Calendar</Link>
        <Link href="/analytics">Analytics</Link>
      </nav>
    </main>
  );
}