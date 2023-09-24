// import CornSvg from "@/../public/corn.svg";
import Link from "next/link";

export default function Nav() {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 flex items-center justify-between p-4 border-b-2 site-secondary-border bg-green-900">
      <div className="flex items-center">
        {/* <CornSvg classname="w-8 h-8" /> */}
        <h1 className="ml-2 font-bold text-lg">Cornucopia</h1>
      </div>
      
      <div className="flex items-center">
        <Link href="/" className="m-2 hover:text-green-400 transition-colors">Dashboard</Link>
        <Link href="/login" className="m-2 hover:text-green-400 transition-colors">Login</Link>
      </div>
    </nav>
  );
};