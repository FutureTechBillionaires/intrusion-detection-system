import Header from './components/Header'; 
import ThreatList from './components/ThreatList';

function App() {
  return (
    
  <div style={{ background: '#0A1929', minHeight: '100vh', color: '#eee' }}> 
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '20px' }}>
      <Header /> 
      <ThreatList />
    </div> 
  </div>
  );
}

export default App;
