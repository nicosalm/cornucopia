import "./globals.css";
import { Geologica, Lexend_Deca } from "next/font/google";
import Nav from "@/app/nav";

// body font
const geologica = Geologica({ subsets: ["latin"] });
// header font
const lexend_deca = Lexend_Deca({ subsets: ["latin"] });

export const metadata = {
  title: "Cornucopia",
  description: "Make open CSA's with other farmers",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={lexend_deca.className + " pt-16"}>
        <Nav />
        {children}
      </body>
    </html>
  );
}
