// Dashboard.js
import React from "react";
const usersData = [
  { id: 1, matricule: "A112233", client: "Ismail", dateEntrer: "10:00h", dateSortie: "12:00h" },
  { id: 2, matricule: "B442233", client: "Mohcine", dateEntrer: "13:00h", dateSortie: "15:00h" },
];

const Dashboard = () => {
  return (
    <div className="container mx-auto mt-8 m-14">

      <div className="flex">
        <div className="w-2/3 bg-white rounded-md p-6 m-4">
          <h3 className="text-xl font-semibold mb-2">Parking statistic</h3>
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

        <div className="w-1/3 bg-white rounded-md p-6 m-4">
          <h3 className="text-xl font-semibold mb-2">Camera Realtime</h3>
          <p className="text-gray-600">Add Camera here</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
