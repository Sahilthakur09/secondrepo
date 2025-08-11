import useSWR from 'swr'

const fetcher = (url: string) => fetch(url).then(r => r.json())

export default function CalendarPage() {
  const { data } = useSWR('http://localhost:8000/api/v1/calendar', fetcher)
  return (
    <main style={{ padding: 24, fontFamily: 'sans-serif' }}>
      <h2>Content Calendar</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  )
}