// Dashboard.js
import React, { useEffect, useRef } from "react";
import io from "socket.io-client";
// import WebCam from "react-webcam"

const usersData = [
  {
    id: 1,
    matricule: "A112233",
    client: "Ismail",
    dateEntrer: "10:00h",
    dateSortie: "Stationnée",
  },
  {
    id: 2,
    matricule: "B442233",
    client: "Mohcine",
    dateEntrer: "13:00h",
    dateSortie: "15:00h",
  },
];

const user = {
  name: "Anas",
  email: "anas@gmail.com",
};

const userRole = JSON.parse(sessionStorage.getItem("user")).role;

const Dashboard = () => {
  console.log("userRole from template, ", userRole);

  // useEffect(() => {
  //   const script = document.createElement("script");
  //   script.src =
  //     "https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.1.3/socket.io.js";
  //   script.async = true;
  //   document.body.appendChild(script);

  //   script.onload = () => {
  //     const socket = io.connect("http://localhost:5000");

  //     socket.on("connected", (msg) => {
  //       console.log(msg);
  //     });

  //     const cameraStream = document.getElementById("camera-stream");

  //     socket.on("image", (frame) => {
  //       cameraStream.src = "data:image/jpg;base64," + frame;
  //     });
  //   };

  //   return () => {
  //     document.body.removeChild(script);
  //   };
  // }, []);

  return (
    <div className="container mx-auto mt-8 m-14">
      <div className="flex">
        <div className="w-2/3 bg-white rounded-md p-6 m-4">
          <h3 className="text-xl font-semibold mb-2">Parking statistic</h3>

          <div className=" flex justify-center items-center">
            <div className="bg-gray-200 rounded-md p-8 px-10 m-4 w-96 ">
              <h3 className="text-xl font-semibold mb-2 text-center">
                New Vehicule
              </h3>
              <p className="text-gray-600 font-semibold">Matricule</p>
              <p className="text-gray-600 font-semibold">Client name</p>
              <p className="text-gray-600 font-semibold">Client name</p>
            </div>
          </div>

          <div className="relative overflow-x-auto shadow-md sm:rounded-lg m-16 mx-5">
            <table className="w-full text-sm text-left rtl:text-right text-gray-700 dark:text-gray-400">
              <thead className="text-xs text-gray-700 uppercase bg-gray-300 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                  <th scope="col" className="px-6 py-3">
                    ID
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Matricule
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Client
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Date Entrer
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Date Sortie
                  </th>
                  <th scope="col" className="px-6 py-3">
                    Action
                  </th>
                </tr>
              </thead>
              <tbody>
                {usersData.map((user) => (
                  <tr
                    key={user.id}
                    className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                  >
                    <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                      {user.id}
                    </td>
                    <td className="px-6 py-4">{user.matricule}</td>
                    <td className="px-6 py-4">{user.client}</td>
                    <td className="px-6 py-4">{user.dateEntrer}</td>
                    <td className="px-6 py-4">{user.dateSortie}</td>
                    <td className="px-6 py-4">
                      <a
                        href="#"
                        className="font-medium text-blue-600 dark:text-blue-500 hover:underline"
                      >
                        Edit
                      </a>
                      <a
                        href="#"
                        className="font-medium text-green-600 dark:text-green-500 hover:underline mx-3"
                      >
                        Consulter
                      </a>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        <div className="w-1/3 bg-white rounded-md p-6 m-4 mb-16">
          <h3 className="text-xl font-semibold mb-10 text-center">Camera Realtime</h3>
          {/* <p className="text-gray-600 text-center">Camera will be here</p> */}
          {/* <WebCam /> */}
          {/* <img
            src="http://localhost:5000/webcam"
            id="camera-stream"
            alt="Camera Stream"
            className="w-full h-auto"
          /> */}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
