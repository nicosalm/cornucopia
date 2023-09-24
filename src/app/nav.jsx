import CornSvg from "@/../public/corn.svg";

export default function Nav() {
  return (
    <nav className="flex items-center justify-between p-4">
      <div className="flex items-center">
        <CornSvg classname="w-8 h-8" />
        <h1 className="ml-2 font-bold text-lg">Cornucopia</h1>
      </div>
      
      <div className="flex items-center">

      </div>
    </nav>
  );
};