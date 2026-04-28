import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-700 text-white px-6 py-3 flex gap-6 items-center shadow">
      <span className="font-bold text-lg">Prog IV - Parcial 1</span>
      <Link to="/" className="hover:underline">Inicio</Link>
      <Link to="/categorias" className="hover:underline">Categorías</Link>
      <Link to="/ingredientes" className="hover:underline">Ingredientes</Link>
      <Link to="/productos" className="hover:underline">Productos</Link>
    </nav>
  );
}
