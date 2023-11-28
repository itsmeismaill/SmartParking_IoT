import axios from "axios";
import { useState, useEffect } from "react";

const Vehicules = () => {
  const [vehiculeData, setVehiculeData] = useState([]);
  const [userData, setUserData] = useState([]);
  const[selectedVehicule, setSelectedVehicule] = useState({
    matricule: "",
    duree: 0,
    montant: 0,
    user_id: null,
    abonnementId: "",
    nduree:0,
  });
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isRenouvellerModalOpen, setIsRenouvellerModalOpen] = useState(false);
  const [newVehiculeData, setNewVehiculeData] = useState({
    matricule: "",
    duree: "",
    montant: "",
    user_id: null,
    abonnementId: "",
  });
  const [currentMontant, setCurrentMontant] = useState(0);

  const getAllVehicules = () => {
    axios
      .get("http://localhost:5000/vehicules")
      .then((response) => {
        console.log("vehicules and users: ", response.data);
        setVehiculeData(response.data[0]);
        setUserData(response.data[1]);
      })
      .catch((error) =>
        console.error("Erreur de récupération des vehicules", error)
      );
  }

  useEffect(() => {
    getAllVehicules()
  }, []);

  const openModal = () => {
    setIsModalOpen(true);
  };
  const openRenouvellerModal = () => {
    setIsRenouvellerModalOpen(true);
  };
  const closeRenouvellerModal = () => {
    setIsRenouvellerModalOpen(false);
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
  const handleInputChange1 = (e) => {
    const { name, value } = e.target;
    setSelectedVehicule((prevUserData) => ({
      ...prevUserData,
      [name]: value,
    }));
    if(name === "nouveauDuree"){
      if(value === ""){
        setCurrentMontant(0)
        return
      }
      setCurrentMontant(((parseFloat(selectedVehicule.duree/60))+parseFloat(value)) * 3)

    }
  };

    const handleUserSelectChange = (e) => {
      
      const { value } = e.target;
      console.log("value, ", value);
      setNewVehiculeData((prevUserData) => ({
        ...prevUserData,
        user_id: value,
      }));
    };
    const handleCreateVehicule = async () => {
      try {
        console.log("Create Vehicule Logic", newVehiculeData);
        const abonnementData = {
          duree: newVehiculeData.duree,
          // montant: newVehiculeData.montant,
        };
        console.log("abonnementData, ", abonnementData);
        const abonnementResponse = await axios.post(
          "http://localhost:5000/abonnements",
          abonnementData );
          console.log("abonnementResponse, ", abonnementResponse.data);
          const newVehicle = {
            matricule: newVehiculeData.matricule,
            abonnementId: abonnementResponse.data.id,
            userId: newVehiculeData.user_id,
          };
          console.log("newVehicle, ", newVehicle);
          const vehiculeResponse = await axios.post(
            "http://localhost:5000/vehicules",
            newVehicle
          );
          console.log("vehiculeResponse, ", vehiculeResponse.data);

          setNewVehiculeData({
            matricule: "",
            duree: "",
            montant: "",
            user_id: "",
            abonnementId: "",
          });
          getAllVehicules()
          closeModal();
    } catch (error) {
      console.error("Error creating vehicule:", error);
    }
  };
  const handleRenouvellerAbonnement = async () => {
    try {
      selectedVehicule["montant"] = currentMontant
      selectedVehicule["duree"] = selectedVehicule.duree + (parseFloat(selectedVehicule["nouveauDuree"]) * 60)
      console.log("Renouveller Abonnement Logic", selectedVehicule);      
      const abonnementData = {
        duree: selectedVehicule["duree"],
        montant: selectedVehicule["montant"],
      };
      const abonnementResponse = await axios.put(
        "http://localhost:5000/abonnements/"+selectedVehicule.abonnementId,
        abonnementData );
        console.log("abonnementResponse, ", abonnementResponse.data);
      
        setSelectedVehicule({
          matricule: "",
          duree: "",
          montant: "",
          user_id: "",
          abonnementId: "",
          nouveauDuree: "",
        });
        getAllVehicules()
        closeRenouvellerModal();
  } catch (error) {
    console.error("Error creating vehicule:", error);
  }
    
    getAllVehicules()
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
              <th scope="col" className="px-6 py-3">
                Durée Abonnement
              </th>
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
                <td className="px-6 py-4">{Vehicule.username}</td>
                <td className="px-6 py-4">{Math.round(Vehicule.duree_abonnement/60)}h</td>
                <td className="px-6 py-4">
                  <a
                    href="#"
                    className="font-medium text-blue-600 dark:text-blue-500 hover:underline"
                    onClick={() => {
                      openRenouvellerModal()
                      console.log("Vehicule, ", Vehicule);
                      setSelectedVehicule({
                        matricule: Vehicule.matricule,
                        duree: Vehicule.duree_abonnement,
                        montant: Vehicule.montant, 
                        user_id: Vehicule.user_id,
                        abonnementId: Vehicule.abonnement_id,
                      })
                    }}
                  >
                    Renouveller Abonnement
                  </a>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      {isRenouvellerModalOpen && (
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
                  <input disabled
                    type="text"
                    id="matricule"
                    name="matricule"
                    value={selectedVehicule.matricule}
                    onChange={handleInputChange1}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>

                <div className="mb-6">
                  <label htmlFor="duree" className="block text-gray-600 mb-2">
                    Durée restante (en heures)
                  </label>
                  <input disabled
                    type="text"
                    id="duree"
                    name="duree"
                    value={selectedVehicule.duree/60}
                    onChange={handleInputChange1}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>
                <div className="mb-6">
                  <label htmlFor="nouveauDuree" className="block text-gray-600 mb-2">
                    Durée ajoutée (en heures)
                  </label>
                  <input 
                    type="text"
                    id="nouveauDuree"
                    value={selectedVehicule.nduree}
                    name="nouveauDuree"
                    onChange={handleInputChange1}
                    className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  />
                </div>

                <div className="mb-6">
                  <label htmlFor="montant" className="block text-gray-600 mb-2">
                    Montant
                  </label>
                  <input disabled
                    type="text"
                    id="montant"
                    name="montant"
                    value={currentMontant}
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
                    onClick={handleRenouvellerAbonnement}
                  >
                    Renouveller
                  </button>
                  <button
                    className="px-4 py-2 ml-2 bg-gray-300 rounded-md hover:bg-gray-400 focus:outline-none"
                    onClick={closeRenouvellerModal}
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

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
                    Client
                  </label>

                  <select
                    value={newVehiculeData.user_id}
                    onChange={handleUserSelectChange}
                    className="mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
                  >
                    {userData.map((user) => (
                      <option key={user.id} value={user.id}>
                        {user.username}
                      </option>
                    ))}
                  </select>
                </div>
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
                  <input disabled
                    type="text"
                    id="montant"
                    name="montant"
                    value={newVehiculeData.duree * 3}
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
