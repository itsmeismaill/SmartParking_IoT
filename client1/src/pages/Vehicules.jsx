// import axios from "axios";
// import { useState, useEffect } from "react";

// const Users = () => {
//   const [vehiculeData, setvehiculeData] = useState([]);
//   const [isModalOpen, setIsModalOpen] = useState(false);
//   const [newvehiculeData, setNewvehiculeData] = useState({
//     matricule: "",
//     userId: "",
//     abonnementId: "",
//   });

//   useEffect(() => {
//     axios("http://localhost:5000/vehicules")
//       .then((response) => {
//         console.log("vehicules: ", response.data);
//         set(response.data);
//       })
//       .catch((error) =>
//         console.error("Erreur de récupération des utilisateurs", error)
//       );
//   }, []);

//   const openModal = () => {
//     setIsModalOpen(true);
//   };

//   const closeModal = () => {
//     setIsModalOpen(false);
//   };

//   const handleInputChange = (e) => {
//     const { name, value } = e.target;
//     setNewUserData((prevUserData) => ({
//       ...prevUserData,
//       [name]: value,
//     }));
//   };

//   const handleCreateUser = () => {
//     // Implement the logic for creating a user with newUserData

//     console.log("Create User Logic", newUserData);
//     axios.post("http://localhost:5000/users", newUserData).then((response) => {
//       console.log(response.data);
//     });

//     closeModal();
//   };

//   return (
//     <div className="relative overflow-x-auto shadow-md sm:rounded-lg m-8 p-4 bg-gray-100 dark:bg-gray-800">
//       <div className="flex justify-between items-center mb-4">
//         <h2 className="text-xl font-bold text-gray-800 dark:text-white">
//           User Management
//         </h2>
//         <button
//           className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none"
//           onClick={openModal}
//         >
//           Create User
//         </button>
//       </div>

//       <div className="relative overflow-x-auto max-h-96">
//         <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
//           <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
//             <tr>
//               <th scope="col" className="px-6 py-3">
//                 ID
//               </th>
//               <th scope="col" className="px-6 py-3">
//                 Name
//               </th>
//               <th scope="col" className="px-6 py-3">
//                 Email
//               </th>
//               <th scope="col" className="px-6 py-3">
//                 Role
//               </th>
//               <th scope="col" className="px-6 py-3">
//                 Action
//               </th>
//             </tr>
//           </thead>
//           <tbody>
//             {userData.map((user) => (
//               <tr
//                 key={user.id}
//                 className="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
//               >
//                 <td className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
//                   {user.id}
//                 </td>
//                 <td className="px-6 py-4">{user.username}</td>
//                 <td className="px-6 py-4">{user.email}</td>
//                 <td className="px-6 py-4">{user.role}</td>
//                 <td className="px-6 py-4">
//                   <a
//                     href="#"
//                     className="font-medium text-blue-600 dark:text-blue-500 hover:underline"
//                   >
//                     Edit
//                   </a>
//                   <a
//                     href="#"
//                     className="font-medium text-green-600 dark:text-green-500 hover:underline mx-3"
//                   >
//                     Consulter
//                   </a>
//                 </td>
//               </tr>
//             ))}
//           </tbody>
//         </table>
//       </div>

//       {/* Modal for creating a new user */}
//       {isModalOpen && (
//         <div className="fixed z-10 inset-0 overflow-y-auto">
//           <div className="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
//             <div
//               className="fixed inset-0 transition-opacity"
//               aria-hidden="true"
//             >
//               <div className="absolute inset-0 bg-gray-500 opacity-75"></div>
//             </div>

//             {/* Modal content */}
//             <div className="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
//               <div className="bg-gray-50 p-4">
//                 <h2 className="text-xl font-bold mb-4">Create User</h2>

//                 {/* Input fields for user information */}
//                 <div className="mb-6">
//                   <label
//                     htmlFor="username"
//                     className="block text-gray-600 mb-2"
//                   >
//                     Username
//                   </label>
//                   <input
//                     type="text"
//                     id="username"
//                     name="username"
//                     value={newUserData.username}
//                     onChange={handleInputChange}
//                     className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
//                   />
//                 </div>

//                 <div className="mb-4">
//                   <label
//                     htmlFor="password"
//                     className="block text-gray-600 mb-2"
//                   >
//                     Password
//                   </label>
//                   <input
//                     type="password"
//                     id="password"
//                     name="password"
//                     value={newUserData.password}
//                     onChange={handleInputChange}
//                     className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
//                   />
//                 </div>

//                 <div className="mb-4">
//                   <label htmlFor="cin" className="block text-gray-600 mb-2">
//                     CIN
//                   </label>
//                   <input
//                     type="text"
//                     id="cin"
//                     name="cin"
//                     value={newUserData.cin}
//                     onChange={handleInputChange}
//                     className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
//                   />
//                 </div>

//                 <div className="mb-4">
//                   <label
//                     htmlFor="telephone"
//                     className="block text-gray-600 mb-2"
//                   >
//                     Telephone
//                   </label>
//                   <input
//                     type="text"
//                     id="telephone"
//                     name="telephone"
//                     value={newUserData.telephone}
//                     onChange={handleInputChange}
//                     className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
//                   />
//                 </div>

//                 <div className="mb-4">
//                   <label htmlFor="email" className="block text-gray-600 mb-2">
//                     Email
//                   </label>
//                   <input
//                     type="email"
//                     id="email"
//                     name="email"
//                     value={newUserData.email}
//                     onChange={handleInputChange}
//                     className="form-input mt-1 p-3 block w-full rounded-md border-2 border-gray-300 focus:outline-none focus:border-blue-500"
//                   />
//                 </div>

//                 {/* Buttons for Create and Cancel actions */}
//                 <div className="flex justify-end">
//                   <button
//                     className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none"
//                     onClick={handleCreateUser}
//                   >
//                     Create
//                   </button>
//                   <button
//                     className="px-4 py-2 ml-2 bg-gray-300 rounded-md hover:bg-gray-400 focus:outline-none"
//                     onClick={closeModal}
//                   >
//                     Cancel
//                   </button>
//                 </div>
//               </div>
//             </div>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// };

// export default Users;
