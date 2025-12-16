  import React, { useState } from 'react';
  export default function ThreatList() { 
    // Mock data for now 
    const threats = [ 
      { id: 1, type: 'SQL Injection', severity: 'high', ip: '192.168.1.100' }, 
      { id: 2, type: 'Brute Force', severity: 'critical', ip: '10.0.0.45' }, 
      { id: 3, type: 'Port Scan', severity: 'medium', ip: '172.16.0.20' } 
    ]; 
     
    const getSeverityColor = (severity) => { 
      switch(severity) { 
        case 'critical': return '#ff4444'; 
        case 'high': return '#ff8844'; 
        case 'medium': return '#ffbb44'; 
        default: return '#44ff44'; 
      } 
    }; 
    
    const [hoveredId, setHoveredId] = useState(null);
    return ( 
      <div style={{ padding: '20px' }}> 
        <h2>Recent Threats</h2> 
        {threats.map(threat => ( 
          <div key={threat.id} style={{ 
            background: '#122438', 
            margin: '20px 0', 
            padding: '20px', 
            borderRadius: '10px', 
            borderLeft: `5px solid ${getSeverityColor(threat.severity)}`,
            boxShadow: '0 2px 10px rgba(0, 0, 0, 0.7)', 
            transition: 'all 0.3s ease-in-out'
          }}> 
            <h3>{threat.type}</h3> 
            <p>IP: {threat.ip} | Severity: {threat.severity.toUpperCase()}</p> 
          </div> 
        ))} 
      </div> 
    ); 
  }