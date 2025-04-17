import { useState } from 'react';
import './App.css';
import { useEffect } from 'react';

const Timer = ({appendLaps, refreshQuote}) => {

    const [time, setTime] = useState(10 * 60);
    
    const [lap, setLap] = useState({startTime: null, endTime: null});


    const [clockStatus, setClockStatus] = useState(false);
    const start = () => {
        setClockStatus(true)
        setLap((prev) => ({ ...prev, startTime: new Date() }));
    };
    const stop = () => {
        setClockStatus(false)
        setLap((prev) => ({...prev, endTime: new Date()}));
    };

    const reset = () => {
        setClockStatus(false);
        
        if (lap.startTime && !lap.endTime) {
            const updatedLap = {...lap, endTime: new Date()};
            appendLaps(updatedLap);
        } else if (lap.startTime && lap.endTime) {
            appendLaps(lap);
        }
        
        setTime(25*60);
        setLap({startTime: null, endTime: null});
        
        // Refresh quote when reset is pressed
        refreshQuote();
    }

    useEffect(()=>{
        if(!clockStatus) return;
        const interval = setInterval(()=>setTime((prev)=>prev - 1),1000)
        return () => clearInterval(interval);
    }, [clockStatus]);

    const formatTime = (time) => {
        let minutes = Math.floor(time / 60);
        let seconds = time % 60;
        if (seconds < 10){seconds = `0${seconds}`};
        if (minutes < 10) { minutes = `0${minutes}` };
        return {minutes, seconds}
    }

    return (
    <div className="timer-wrapper">
        <div className="timer-display">
        <span className="timer-digits">{formatTime(time).minutes}</span>
        <span className="timer-colon">:</span>
        <span className="timer-digits">{formatTime(time).seconds}</span>
        </div>
        <div className="timer-buttons">
        <button className="timer-btn" onClick={start}>Start</button>
        <button className="timer-btn" onClick={stop}>Stop</button>
        <button className="timer-btn" onClick={reset}>Reset</button>
        </div>
    </div>
    );
};

export default Timer;
