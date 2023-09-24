import Dashboard from "./dashboard/Dashboard"
import Login from "./login/page"
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        <Dashboard/>
      </div>
    </main>
  )
}
