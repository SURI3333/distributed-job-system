import { useState } from "react";
import axios from "axios";

function SubmitJob() {
  const [jobType, setJobType] = useState("");

  const submitJob = async () => {
    await axios.post("http://127.0.0.1:8000/jobs", {
      job_type: jobType,
      payload: { data: "test" },
      priority: 1
    });

    alert("Job Submitted");
  };

  return (
    <div>
      <h2>Submit Job</h2>

      <input
        type="text"
        placeholder="Enter job type"
        value={jobType}
        onChange={(e) => setJobType(e.target.value)}
      />

      <button onClick={submitJob}>Submit</button>
    </div>
  );
}

export default SubmitJob;
