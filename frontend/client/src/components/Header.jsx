export default function Header() { 
    return ( 
      <header style={{ 
        background: '#0F2033', 
        color: '#B3D9FF', 
        padding: '30px', 
        textAlign: 'center' 
      }}> 
        <h1 style={{ fontSize: '2.5em', marginBottom: '5px'}}>      AI Intrusion Detection System</h1> 
        <p style ={{ color: '#aaa', fontSize: '1.2em'}}>
          Real-time Security Monitoring
        </p> 
      </header> 
    ); 
  }