// Dashboard.js
import axios from "axios";
import React, { useEffect, useRef, useState } from "react";
import io from "socket.io-client";
import Vehicules from "../pages/Vehicules";

import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { formatDistanceToNow } from 'date-fns';
import { Navigate, useNavigate } from "react-router";
import { render } from "@testing-library/react";
import { get } from "lodash";

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

let userRole;

if (sessionStorage.getItem("user")) {
  userRole = JSON.parse(sessionStorage.getItem("user")).role;
}

const Dashboard = () => {
  const navigate = useNavigate();
  const [vehiculeData, setVehiculeData] = useState([]);
  const [enteredVehiculeData, setEnteredVehiculeData] = useState({
    matricule: "",
    clientName: "",
    date_entree: "",
    date_sortie: "",
  });

  console.log("userRole from template, ", userRole);

  const socket = useRef();

  function getTimeParkingWithVehicule(){
    axios
      .get("http://localhost:5000/timeparkings")
      .then((response) => {
        console.log("vehicules: ", response.data);
        setVehiculeData(response.data);
      })
      .catch((error) =>
        console.error("Erreur de récupération des vehicules", error)
      );
  }

  useEffect(() => {

    getTimeParkingWithVehicule();

    socket.current = io.connect("http://localhost:5000");

    socket.current.on("connected", (msg) => {
      console.log(msg);
    });

    socket.current.on("car_event", (data) => {
      console.log(data.message);
      console.log(data?.timeparking);
      console.log("Timeparking data:", data.timeparking?.matricule);
      console.log("Timeparking data:", data.timeparking?.matricule);
      console.log("Timeparking data:", data.timeparking?.matricule);

      // console.log("state, ", data.timeparking?.matricule);

      if(data.timeparking.duree == 0){

        setEnteredVehiculeData({
          matricule: data.timeparking?.matricule,
          clientName: data.timeparking.clientName,
          date_entree: "",
          date_sortie: "",
        });

        return toast.warning(data.message, { position: toast.POSITION.TOP_CENTER });

        
        // getTimeParkingWithVehicule();
      }

      const dateTimeEntree = new Date(data.timeparking.date_entree);

      const dateTimeSortie = data.timeparking.date_sortie != "Stationed" ? new Date(data.timeparking.date_sortie) : "Stationed";

      // Format date to "time ago" format
      const timeAgoEntree = formatDistanceToNow(dateTimeEntree, { addSuffix: true });
      const timeAgoSortie = dateTimeSortie != "Stationed" ? formatDistanceToNow(dateTimeSortie, { addSuffix: true }) : dateTimeSortie;

      setEnteredVehiculeData({
        matricule: data.timeparking.matricule,
        clientName: data.timeparking.clientName,
        date_entree: timeAgoEntree,
        date_sortie: timeAgoSortie,
      });


      // setEnteredVehiculeData({
      //   matricule: data.timeparking.matricule,
      //   clientName: data.timeparking.clientName,
      //   date_entree: timeAgo,
      //   date_sortie: data.timeparking.date_sortie,
      // });

  

      toast.success(data.message, { position: toast.POSITION.TOP_CENTER });

      getTimeParkingWithVehicule();
      
    });
    // render(<Navigate to="/dashboard" />);

    return () => {
      socket.current.disconnect();
    };
    
  }, []);

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
      <ToastContainer />
      <div className="flex">
        <div className="w-2/3 bg-white rounded-md p-6 m-4">
          <h3 className="text-xl font-semibold mb-2">Parking statistic</h3>

          <div className="flex justify-center items-center">
            <div className="bg-gray-200 rounded-md p-8 px-10 m-4 w-96">
              <h3 className="text-xl font-semibold mb-4 text-center">
                New Vehicle
              </h3>
              <div className="info-item flex">
                <p className="text-gray-600 font-semibold">Matricule</p>
                <span className="text-blue-500 font-semibold mx-auto">
                  {enteredVehiculeData.matricule}
                </span>
              </div>
              <div className="info-item flex">
                <p className="text-gray-600 font-semibold">Client Name</p>
                <span className="text-blue-500 font-semibold mx-auto">
                  {enteredVehiculeData.clientName}
                </span>
              </div>
              <div className="info-item flex">
                <p className="text-gray-600 font-semibold">Date Entrée</p>
                <span className="text-blue-500 font-semibold mx-auto">
                  {enteredVehiculeData.date_entree}
                </span>
              </div>
              <div className="info-item flex">
                <p className="text-gray-600 font-semibold">Date Sortie</p>
                <span className="text-blue-500 font-semibold mx-auto">
                  {enteredVehiculeData.date_sortie}
                </span>
              </div>
            </div>
          </div>

          <div className="relative overflow-x-auto shadow-md sm:rounded-lg m-16 mx-5">
            {/* <Vehicules /> */}
            <div className="relative overflow-x-auto max-h-96">

            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" className="px-6 py-3">
                ID
              </th>
              <th scope="col" className="px-6 py-3">
                Matricule
              </th>
              <th scope="col" className="px-6 py-3">
                Client Name
              </th>
              <th scope="col" className="px-6 py-3">
                Durée Abonnement
              </th>
              <th scope="col" className="px-6 py-3">
                Date Entrée
              </th>
              <th scope="col" className="px-6 py-3">
                Date Sortie
              </th>
              {/* <th scope="col" className="px-6 py-3">
                Action
              </th> */}
            </tr>
          </thead>
          <tbody>
            {vehiculeData.map((Vehicule) => (
              <tr
                key={Vehicule.id}
                className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
              >
                <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                  {Vehicule.id}
                </td>
                <td className="px-6 py-4">{Vehicule.matricule}</td>
                {/* <td className="px-6 py-4">{Vehicule.user.username}</td> */}
                <td className="px-6 py-4">{Vehicule.clientName}</td>
                <td className="px-6 py-4">{Vehicule.duree}</td>
                <td className="px-6 py-4">{Vehicule.date_entree}</td>
                <td className="px-6 py-4">{Vehicule.date_sortie}</td>
                <td className="px-6 py-4">
                  {/* <a
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
                  </a> */}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        </div>
          </div>
        </div>

        <div className="w-1/3 bg-white rounded-md p-6 m-4 mb-16">
          <h3 className="text-xl font-semibold mb-10 text-center">
            Camera Realtime
          </h3>
          {/* <p className="text-gray-600 text-center">Camera will be here</p> */}
          {/* <WebCam /> */}
          <img
            src="http://localhost:5000/webcam"
            id="camera-stream"
            alt="Camera Stream"
            className="w-full h-auto"
          />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
