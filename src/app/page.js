import Dashboard from "./dashboard/Dashboard"
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <Dashboard/>
      </div>
    </main>
  )
}
