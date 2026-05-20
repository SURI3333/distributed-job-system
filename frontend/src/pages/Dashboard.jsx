import { useEffect, useState } from "react";
import axios from "axios";

function Dashboard() {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/jobs")
      .then(res => setJobs(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Jobs Dashboard</h2>

      {jobs.map(job => (
        <div key={job.id}>
          <p>ID: {job.id}</p>
          <p>Type: {job.job_type}</p>
          <p>Status: {job.status}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default Dashboard;