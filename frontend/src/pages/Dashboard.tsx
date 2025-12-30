import api from "../api/api";
import { useEffect, useState } from "react";

const Dashboard = () => {
  
  const [rooms, setRooms] = useState<any[]>([]);
  const [ContextMenu, setContextMenu] = useState<{
    x: number;
    y:number;
    room:any
  } | null>(null);

  useEffect(() => {
    api
      .get("/dashboard/rooms")
      .then((res) => setRooms(res.data))
      .catch((err) => console.error(err));
  }, []);

//console.log("rooms:", rooms);

const handleRightClick = (
  e: React.MouseEvent,
  room: any
) => {
  e.preventDefault();
  setContextMenu({
    x : e.clientX,
    y: e.clientY,
    room,
  });
};

useEffect(() => {
  const closeMenu = () => setContextMenu(null);
  window.addEventListener("click",closeMenu)
  return () => window.removeEventListener("click", closeMenu);
}, []);


  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6">
      <h1 className="text-4xl font-mont font-black pb-10 pointer-events-none">
        Dashboard
      </h1>
      <h2 className="text-lg font-inter pb-7">
     Right click for more options
      </h2>

      <div className="grid
  grid-cols-2
  sm:grid-cols-3
  md:grid-cols-4
  gap-4
  justify-items-center">
        {rooms.map((room) => {
          const bg =
            room.status === "empty"
              ? "bg-[#f8f8f8]"
              : room.status === "occupied"
              ? "bg-[#7FFF92]"
              : "bg-[#FF9494]";

          return (
            <div
              key={room.room_id}
              onContextMenu={(e) => handleRightClick(e, room)}
              className={`relative w-32 h-32 md:w-40 md:h-40
                          ${bg} border border-black/20
                          rounded-xl flex items-center justify-center
                          font-inter text-xs
                          transition-all duration-300
                          hover:scale-[1.02] cursor-pointer`}
            >
              {/* CENTER CONTENT */}
              {room.status === "empty" ? (
                <span className="text-3xl text-[#7a7a7a]">+</span>
              ) : (
                <div className="text-center">
                  <p className="font-semibold">{room.tenant?.name}</p>
                  <p>{room.tenant?.phone}</p>
                </div>
              )}

              {/* ROOM NUMBER */}
              <div className="absolute bottom-3">
                Room {room.room_id}
              </div>
            </div>
          );
        })}
      </div>

        {ContextMenu && (
  <div
    style={{
      top: ContextMenu.y,
      left: ContextMenu.x,
    }}
    className="
      fixed z-50 w-56
      bg-[#e8e8e8]
      rounded-lg
      shadow-[0_8px_24px_rgba(0,0,0,0.25)]
      overflow-hidden
      text-sm text-black
    "
  >
    {/* EMPTY ROOM */}
    {ContextMenu.room.status === "empty" && (
      <>
        <MenuItem label="Add Tenant" onClick={() => setContextMenu(null)} />
        <Divider />
        <MenuItem label="View Room Details" onClick={() => setContextMenu(null)} />
      </>
    )}

    {/* OCCUPIED ROOM */}
    {["occupied", "due"].includes(ContextMenu.room.status) && (
      <>
        <MenuItem label="Payment" onClick={() => setContextMenu(null)} />
        <Divider />
        <MenuItem label="Miscellaneous" onClick={() => setContextMenu(null)} />

        {ContextMenu.room.room_id > 5 && (
          <>
            <Divider />
            <MenuItem label="Electrical bill" onClick={() => setContextMenu(null)} />
            <Divider />
            <MenuItem label="Water bill" onClick={() => setContextMenu(null)} />
          </>
        )}

        <Divider />
        <MenuItem
          label="Check out"
          danger
          onClick={() => setContextMenu(null)}
        />
        <Divider />
        <MenuItem label="View report" onClick={() => setContextMenu(null)} />
      </>
    )}
  </div>
)}


    </div>
  );
};


const Divider = () => (
  <div className="h-px bg-black/20 mx-2" />
);


const MenuItem = ({
  label,
  onClick,
  danger = false,
}: {
  label: string;
  onClick: () => void;
  danger?: boolean;
}) => (
  <button
    onClick={onClick}
    className={`
      w-full px-4 py-2 text-left
      hover:bg-white/30
      transition-colors
      ${danger ? "text-red-600" : ""}
    `}
  >
    {label}
  </button>
);

export default Dashboard;
