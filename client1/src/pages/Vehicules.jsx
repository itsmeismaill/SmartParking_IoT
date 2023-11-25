import axios from "axios";
import { useState, useEffect } from "react";

const Vehicules = () => {
  const [vehiculeData, setVehiculeData] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newVehiculeData, setNewVehiculeData] = useState({
    matricule: "",
    duree: "",
    montant: "",
    // userId: "",
    abonnementId: "",
  });

  useEffect(() => {
    axios.get("http://localhost:5000/vehicules", { withCredentials: true })
      .then((response) => {
        console.log("vehicules: ", response.data);
        setVehiculeData(response.data);
      })
      .catch((error) =>
        console.error("Erreur de récupération des vehicules", error)
      );
  }, []);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewVehiculeData((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
  };

  const handleCreateVehicule = () => {
    console.log("Create Vehicule Logic", newVehiculeData);

    const abonnementData = {
      duree: newVehiculeData.duree,
      montant: newVehiculeData.montant,
      inital_duree: newVehiculeData.duree,

    };

    // console.log("abonnementData, ", abonnementData);

    axios
      .post("http://localhost:5000/abonnements", abonnementData, {
        withCredentials: true,
      })
      .then((response) => {
        console.log("data, ", response.data);
        console.log("id, ", response.data.id);

        setNewVehiculeData({
          abonnementId: response.data.id,
        });

        // axios
        //   .post("http://localhost:5000/vehicules", newVehicle, {
        //     withCredentials: true,
        //   })
        //   .then((response) => {
        //     console.log(response.data);
        //   });
      });

    const newVehicle = {
      matricule: newVehiculeData.matricule,
      abonnementId: newVehiculeData.abonnementId,
    };

    console.log("newVehicle, ", newVehicle);

    axios
      .post("http://localhost:5000/vehicules", newVehicle, {
        withCredentials: true,
      })
      .then((response) => {
        console.log(response.data);
      });

    closeModal();
  };

  return (
    <div className="relative overflow-x-auto shadow-md sm:rounded-lg m-8 p-4 bg-gray-100 dark:bg-gray-800">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-bold text-gray-800 dark:text-white">
          Vehicule Management
        </h2>
        <button
          className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none"
          onClick={openModal}
        >
          Create Vehicule
        </button>
      </div>

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
              {/* <th scope="col" className="px-6 py-3">
                Role
              </th> */}
              <th scope="col" className="px-6 py-3">
                Action
              </th>
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
                {/* <td className="px-6 py-4">{user.role}</td> */}
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

      {/* Modal for creating a new user */}
      {isModalOpen && (
        <div className="fixed z-10 inset-0 overflow-y-auto">
          <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
            <div
              className="fixed inset-0 transition-opacity"
              aria-hidden="true"
            >
              <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
            </div>

            {/* Modal content */}
            <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
              <div className="bg-gray-50 p-4">
                <h2 className="text-xl font-bold mb-4">Create Vehicule</h2>

                {/* Input fields for user information */}
                <div className="mb-6">
                  <label
                    htmlFor="matricule"
                    className="block text-gray-600 mb-2"
                  >
                    Matricule
                  </label>
                  <input
                    type="text"
                    id="matricule"
                    name="matricule"
                    value={newVehiculeData.matricule}
                    onChange={handleInputChange}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>

                <div className="mb-6">
                  <label htmlFor="duree" className="block text-gray-600 mb-2">
                    Durée
                  </label>
                  <input
                    type="text"
                    id="duree"
                    name="duree"
                    value={newVehiculeData.duree}
                    onChange={handleInputChange}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>

                <div className="mb-6">
                  <label htmlFor="montant" className="block text-gray-600 mb-2">
                    Montant
                  </label>
                  <input
                    type="text"
                    id="montant"
                    name="montant"
                    value={newVehiculeData.montant}
                    onChange={handleInputChange}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>

                {/* <div className="mb-4">
                  <label htmlFor="email" className="block text-gray-600 mb-2">
                    Client Name
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    value={newUserData.email}
                    onChange={handleInputChange}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div> */}

                {/* Buttons for Create and Cancel actions */}
                <div className="flex justify-end">
                  <button
                    className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none"
                    onClick={handleCreateVehicule}
                  >
                    Create
                  </button>
                  <button
                    className="px-4 py-2 ml-2 bg-gray-300 rounded-md hover:bg-gray-400 focus:outline-none"
                    onClick={closeModal}
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Vehicules;
