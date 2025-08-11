import { useState } from 'react'

export default function Generate() {
  const [body, setBody] = useState('')
  const [result, setResult] = useState<any>(null)
  const [loading, setLoading] = useState(false)

  async function handleGenerate() {
    setLoading(true)
    const res = await fetch('http://localhost:8000/api/v1/content/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        industry: 'Technology',
        role: 'Product Manager',
        interests: ['AI', 'SaaS'],
        brand_voice: 'Professional and friendly',
        format: 'text',
        topic_hint: body || 'product discovery',
        language: 'en'
      })
    })
    const data = await res.json()
    setResult(data)
    setLoading(false)
  }

  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Generate Content</h2>
      <textarea rows={4} style={{ width: '100%', marginBottom: 12 }} placeholder="Topic or hint" value={body} onChange={e => setBody(e.target.value)} />
      <button onClick={handleGenerate} disabled={loading}>{loading ? 'Generating...' : 'Generate'}</button>
      {result && (
        <div style={{ marginTop: 16 }}>
          {result.title && <h3>{result.title}</h3>}
          <p>{result.body}</p>
          <p><strong>Hashtags:</strong> {result.hashtags?.join(' ')}</p>
          {result.call_to_action && <p><em>{result.call_to_action}</em></p>}
        </div>
      )}
    </main>
  )
}