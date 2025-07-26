
import {
    SignInButton,
    SignUpButton,
    SignedIn,
    SignedOut,
    UserButton
} from "@clerk/nextjs";
import Link from "next/link";

const Navbar = () => {
    return (
        <header>
            <div className="flex items-center justify-between p-4 bg-purple-900 text-white w-full rounded-b-lg shadow-md fixed top-0 z-50 px-4">
                <div className="logo">
                    <Link href="/"
                        className="transition-colors duration-200 rounded-lg px-6 py-3 hover:border-purple-300 hover:border-b-2"
                    >FARM Template</Link>
                </div>
                <ul className="flex space-x-4">
                    <li>
                        <Link
                            href="/about"
                            className="transition-colors duration-200 rounded-lg px-3 py-1 hover:bg-purple-300 hover:text-black"
                        >
                            About
                        </Link>
                    </li>
                    <li>
                        <Link
                            href="/contact"
                            className="transition-colors duration-200 rounded-lg px-3 py-1 hover:bg-purple-300 hover:text-black"
                        >
                            Contact
                        </Link>
                    </li>
                </ul>
                <div className="flex items-center space-x-4">
                    <SignedOut>
                        <span className="transition-colors duration-200 rounded-lg px-3 py-1 hover:bg-purple-300 hover:text-black cursor-pointer">
                            <SignInButton />
                        </span>
                        <span className="transition-colors duration-200 rounded-lg px-3 py-1 hover:bg-purple-300 hover:text-black cursor-pointer">
                            <SignUpButton />
                        </span>
                    </SignedOut>
                    <SignedIn>
                        <UserButton />
                    </SignedIn>
                </div>
            </div>
        </header>
    )
}

export default Navbar