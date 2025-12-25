import { MdAlternateEmail } from "react-icons/md";
import { FaFingerprint, FaRegEye, FaRegEyeSlash } from "react-icons/fa";
import { useState } from "react";

const Login = () => {
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const togglePasswordVisibility = () => setShowPassword(!showPassword);

  const [Error, setError] = useState<string | null>(null);

  return (
    <>
      <div className="w-full h-screen flex items-center justify-center">
        <div className="w-[90%] p-5 max-w-sm md:max-w-md lg:max-w-md  bg-white text-black flex flex-col items-center gap-3 rounded-3xl border-[0.5px] border-black/30">
          <h1 className="font-mont font-black tracking-[-0.05em] text-lg md:text-4xl mb-5 mt-10">
            LOGIN
          </h1>
          <div className="w-full flex flex-col gap-3 px-4">
            <div className="w-full flex items-center bg-[#f8f8f8] p-2 rounded-lg gap-2">
              <MdAlternateEmail color="#7a7a7a" />

              <input
                type="text"
                placeholder="Username"
                id="username"
                className="bg-transparent border-0 w-full outline-none text-sm md:text-base placeholder-[#7a7a7a] rounded-lg md:placeholder:text-sm"
              />
            </div>
            <div className="w-full flex items-center bg-[#f8f8f8] p-2 rounded-lg gap-2 relative">
              <FaFingerprint color="#7a7a7a" />
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Password"
                id="pass"
                className="bg-transparent border-0 w-full outline-none text-sm md:text-base placeholder-[#7a7a7a] rounded-lg md:placeholder:text-sm"
              />
              {showPassword ? (
                <FaRegEyeSlash
                  color="#7a7a7a"
                  className="absolute right-5 cursor-pointer"
                  onClick={togglePasswordVisibility}
                />
              ) : (
                <FaRegEye
                  color="#7a7a7a"
                  className="absolute right-5 cursor-pointer"
                  onClick={togglePasswordVisibility}
                />
              )}
            </div>
          </div>

          {Error && (
            <p className="text-red-500 font-inter text-[8px] md:text-xs mt-5 pointer-events-none">
              {Error}
            </p>
          )}


          <button
            type="button"
            className="w-1/3 bg-black
           rounded-lg text-white font-bold font-mont py-2 px-4 my-10"
            onClick={() => setError("Invalid Username or Password")}
          >
            LOGIN
          </button>
        </div>
      </div>
    </>
  );
};

export default Login;
