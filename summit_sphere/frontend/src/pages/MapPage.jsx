import {MapContainer, Marker, Popup, TileLayer} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import "../styles.css";
import {Icon} from "leaflet";

function MapPage() {

  const MountainIcon = new Icon({
    iconUrl: "https://cdn-icons-png.flaticon.com/512/6395/6395508.png",
    iconSize: [38, 38]
  });

  return(
    <MapContainer center={[49.17907, 20.08842]} zoom={13} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://tile.opentopomap.org/{z}/{x}/{y}.png"
      />
      <TileLayer url="https://tile.waymarkedtrails.org/hiking/{z}/{x}/{y}.png" />
      <Marker position={[49.17907, 20.08842]} icon={MountainIcon}>
        <Popup>
          Rysy (2499)
        </Popup>
      </Marker>
  </MapContainer>
  );
}

export default MapPage;