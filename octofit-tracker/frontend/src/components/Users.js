
import { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `${process.env.REACT_APP_CODESPACE_URL}/api/users/`;

  useEffect(() => {
    console.log('Fetching Users from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Fetched Users:', results);
      })
      .catch(err => console.error('Error fetching users:', err))
      .finally(() => setLoading(false));
  }, [endpoint]);

  if (loading) return <div className="text-center my-4">Loading users...</div>;

  if (!users.length) return <div className="alert alert-info">No users found.</div>;

  const columns = Array.from(
    users.reduce((cols, item) => {
      Object.keys(item).forEach(k => cols.add(k));
      return cols;
    }, new Set())
  );

  return (
    <div className="card mb-4">
      <div className="card-header bg-warning text-dark">
        <h2 className="h4 mb-0">Users</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-bordered">
            <thead className="table-light">
              <tr>
                {columns.map(col => <th key={col}>{col}</th>)}
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  {columns.map(col => <td key={col}>{String(user[col] ?? '')}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default Users;
