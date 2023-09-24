import Image from 'next/image'
import Dashboard from './dashboard/page'
import DeliveryManager from './dashboard/DeliveryManager'

export default function Home() {
  return (
    <main>
      <div>
        <DeliveryManager data={null} />
      </div>
    </main>
  )
}
