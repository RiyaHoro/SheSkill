import React, { useEffect, useState } from 'react';
import api from '../services/api';
import SkillGapChart from '../charts/SkillGapChart';

export default function DashboardPage() {
  const [career, setCareer] = useState(null);
  const [gap, setGap] = useState(null);
  const [courses, setCourses] = useState([]);
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    const load = async () => {
      const rec = await api.get('/career-recommendation');
      const sg = await api.get('/skill-gap');
      const crs = await api.get('/courses');
      const jb = await api.get('/jobs');
      setCareer(rec.data);
      setGap(sg.data);
      setCourses(crs.data);
      setJobs(jb.data);
    };
    load();
  }, []);

  if (!career || !gap) return <p>Loading dashboard...</p>;

  return (
    <div className="grid">
      <div className="card">
        <h2>Recommended Career</h2>
        <h3>{career.recommended_career.name}</h3>
        <p>Suitability Score: {career.suitability_score}%</p>
      </div>
      <SkillGapChart requiredCount={gap.required_skills.length} haveCount={gap.user_skills.length} gapCount={gap.skill_gap.length} />
      <div className="card">
        <h3>Courses</h3>
        {courses.map((course) => (
          <div key={course.link} className="list-item">
            <strong>{course.title}</strong>
            <p>{course.provider} | {course.estimated_duration}</p>
            <a href={course.link} target="_blank" rel="noreferrer">View course</a>
          </div>
        ))}
      </div>
      <div className="card">
        <h3>Jobs</h3>
        {jobs.map((job) => (
          <div key={job.link} className="list-item">
            <strong>{job.title}</strong>
            <p>{job.company} | {job.location} | {job.source}</p>
            <a href={job.link} target="_blank" rel="noreferrer">Apply</a>
          </div>
        ))}
      </div>
    </div>
  );
}
