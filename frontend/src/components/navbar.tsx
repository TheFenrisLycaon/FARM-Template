
import {
    SignInButton,
    SignUpButton,
    SignedIn,
    SignedOut,
    UserButton
} from "@clerk/nextjs";
import Link from "next/link";

const linkClasses = "transition-colors duration-200 rounded-lg px-3 py-1 hover:bg-purple-300 hover:text-black";

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
                        <Link href="/about" className={linkClasses}>
                            About
                        </Link>
                    </li>
                    <li>
                        <Link href="/contact" className={linkClasses}>
                            Contact
                        </Link>
                    </li>
                </ul>
                <div className="flex items-center space-x-4">
                    <SignedOut>
                        <div className={`${linkClasses} cursor-pointer`}>
                            <SignInButton />
                        </div>
                        <div className={`${linkClasses} cursor-pointer`}>
                            <SignUpButton />
                        </div>
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