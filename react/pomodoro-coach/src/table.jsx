// table.jsx
import './App.css';

const Table = ({laps}) => {
  return (
    <div className="session-table-wrapper">
      <h2 className="session-title">Completed Sessions</h2>
      <table className="session-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Start Time</th>
            <th>End Time</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
        {laps.map((lap, index) => 
            <tr key={index}>
                <td>{index + 1}</td>
                <td>{lap.startTime?.toLocaleTimeString()}</td>
                <td>{lap.endTime?.toLocaleTimeString()}</td>
                <td>{lap.endTime && lap.startTime ? `${Math.round((lap.endTime - lap.startTime) / 1000 / 60)} mins` : 'N/A'}</td>
            </tr>
        )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
