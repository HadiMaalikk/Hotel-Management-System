import { MdAlternateEmail } from "react-icons/md";
import { FaFingerprint, FaRegEye, FaRegEyeSlash } from "react-icons/fa";
import { useState } from "react";

const Login = () => {
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const togglePasswordVisibility = () => setShowPassword(!showPassword);

  return (
    <>
      <div className="w-full h-screen flex items-center justify-center">
        <div className="w-[90%] p-5 max-w-sm md:max-w-md lg:max-w-md  bg-white text-black flex flex-col items-center gap-3 rounded-3xl border-[0.5px] border-black/50">
          <h1 className="font-mont font-black tracking-[-0.05em] text-lg md:text-3xl my-5">
            LOGIN
          </h1>
          <div className="w-full flex flex-col gap-3">
            <div className="w-full flex items-center bg-[#f8f8f8] p-2 rounded-lg gap-2">
              <MdAlternateEmail />

              <input
                type="text"
                placeholder="Username"
                id="username"
                className="bg-transparent border-0 w-full outline-none text-sm md:text-base placeholder-[#7a7a7a] rounded-lg md:placeholder:text-sm"
              />
            </div>
            <div className="w-full flex items-center bg-[#f8f8f8] p-2 rounded-lg gap-2 relative">
              <FaFingerprint />
              <input
                type={showPassword ? "text" : "password"}
                placeholder="Password"
                id="pass"
                className="bg-transparent border-0 w-full outline-none text-sm md:text-base placeholder-[#7a7a7a] rounded-lg md:placeholder:text-sm"
              />
              {showPassword ? (
                <FaRegEyeSlash
                  className="absolute right-5 cursor-pointer"
                  onClick={togglePasswordVisibility}
                />
              ) : (
                <FaRegEye
                  className="absolute right-5 cursor-pointer"
                  onClick={togglePasswordVisibility}
                />
              )}
            </div>
          </div>
          <p className="text-red-500 font-inter text-[8px] md:text-xs my-5">
            Invalid Username or Password
          </p>

          <button></button>
        </div>
      </div>
    </>
  );
};

export default Login;
