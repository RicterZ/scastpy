HTTP_TEMPLATE = '''<?xml version="1.0"?>
<root xmlns="urn:schemas-upnp-org:device-1-0">
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    <device>
        <deviceType>urn:schemas-upnp-org:device:MediaRenderer:1</deviceType>
        <presentationURL>/</presentationURL>
        <friendlyName>ScastPy</friendlyName>
        <dlna:X_DLNADOC xmlns:dlna="urn:schemas-dlna-org:device-1-0">DMR-1.50</dlna:X_DLNADOC>
        <UDN>uuid:3eddf2ee-0715-4e69-ac4c-2e6593a5d79a</UDN>
        <serviceList>
            <service>
                <serviceType>urn:schemas-upnp-org:service:AVTransport:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:AVTransport</serviceId>
                <controlURL>_urn:schemas-upnp-org:service:AVTransport_control</controlURL>
                <SCPDURL>_urn:schemas-upnp-org:service:AVTransport_scpd.xml</SCPDURL>
                <eventSubURL>_urn:schemas-upnp-org:service:AVTransport_event</eventSubURL>
            </service>
            <service>
                <serviceType>urn:schemas-upnp-org:service:RenderingControl:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:RenderingControl</serviceId>
                <controlURL>_urn:schemas-upnp-org:service:RenderingControl_control</controlURL>
                <SCPDURL>_urn:schemas-upnp-org:service:RenderingControl_scpd.xml</SCPDURL>
                <eventSubURL>_urn:schemas-upnp-org:service:RenderingControl_event</eventSubURL>
            </service>
            <service>
                <serviceType>urn:schemas-upnp-org:service:ConnectionManager:1</serviceType>
                <serviceId>urn:upnp-org:serviceId:ConnectionManager</serviceId>
                <SCPDURL>_urn:schemas-upnp-org:service:ConnectionManager_scpd.xml</SCPDURL>
                <controlURL>_urn:schemas-upnp-org:service:ConnectionManager_control</controlURL>
                <eventSubURL>_urn:schemas-upnp-org:service:ConnectionManager_event</eventSubURL>
            </service>
        </serviceList>
        <manufacturer>Microsoft Corporation</manufacturer>
        <manufacturerURL>http://www.microsoft.com</manufacturerURL>
        <modelDescription>Media Renderer</modelDescription>
        <modelName>Windows Media Player</modelName>
        <modelURL>http://go.microsoft.com/fwlink/?Linkld=105927</modelURL>
    </device>
    <URLBase>http://{}:{}</URLBase>
</root>'''

SSDP_TEMPLATE = '''HTTP/1.1 200 OK\r
LOCATION: {location}\r
X-User-Agent: scastpy\r
ST: {st}\r
USN: {usn}\r
\r
'''

COMMON_RESPONSE = ''

