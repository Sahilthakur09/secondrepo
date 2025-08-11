import Link from 'next/link'

export default function Home() {
  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h1>Influence OS</h1>
      <p>LinkedIn Personal Branding AI - Demo Dashboard</p>
      <ul>
        <li><a href="http://localhost:8000/api/docs" target="_blank" rel="noreferrer">Open API Docs</a></li>
        <li><Link href="/generate">Generate Content</Link></li>
        <li><Link href="/calendar">Content Calendar</Link></li>
        <li><Link href="/analytics">Analytics</Link></li>
      </ul>
    </main>
  )
}