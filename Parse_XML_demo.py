'''

IOS XR
Netconf query to get Tunnel tables , parese the tables XML and get the tunnel ID , 
Netconf setup static route to Tunnel ID
Traffice engineering done


Created on Jan 15, 2016

@author: AlexFeng
'''
import paramiko
import time
import xml.etree.cElementTree as ET

Set_route_TE='''<?xml version="1.0" encoding="UTF-8"?>
<rpc message-id="102" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<edit-config>
<target>
<candidate/>
</target>
<config>
<Configuration>
            <RouterStatic MajorVersion="4" MinorVersion="0">
                <DefaultVRF>
                    <AddressFamily>
                        <VRFIPV4>
                            <VRFUnicast>
                                <VRFPrefixTable>
                                    <VRFPrefix>
                                        <Naming>
                                            <Prefix>
                                                <IPV4Address>
                                                    2.2.2.2
                                                </IPV4Address>
                                            </Prefix>
                                            <PrefixLength>
                                                32
                                            </PrefixLength>
                                        </Naming>
                                        <VRFRoute>
                                            <VRFNextHopTable>
                                                <VRFNextHop>
                                                    <Naming>
                                                        <InterfaceName>
                                                            tunnel-te%s
                                                        </InterfaceName>
                                                    </Naming>
                                                </VRFNextHop>
                                            </VRFNextHopTable>
                                        </VRFRoute>
                                    </VRFPrefix>
                                </VRFPrefixTable>
                            </VRFUnicast>
                        </VRFIPV4>
                    </AddressFamily>
                </DefaultVRF>
            </RouterStatic>
</Configuration>
</config>
</edit-config>
<commit/>
</rpc>]]>]]>'''


Get_PCEP_LSP_Result='''<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <data>
        <Operational>
            <MPLS_PCE MajorVersion="4" MinorVersion="5">
                <LSPTable>
                    <LSP>
                        <Naming>
                            <SymbolicName>
                                rsvp-te3
                            </SymbolicName>
                        </Naming>
                        <SourceAddress>
                            192.168.0.3
                        </SourceAddress>
                        <DestinationAddress>
                            192.168.0.6
                        </DestinationAddress>
                        <SymbolicName>
                            rsvp-te3
                        </SymbolicName>
                        <SessionInternalLspID>
                            7009
                        </SessionInternalLspID>
                        <StatefulRequestParameterID>
                            0
                        </StatefulRequestParameterID>
                        <RequestQueueSize>
                            0
                        </RequestQueueSize>
                        <Creator>
                            <NodeIdentifier>
                                Not set
                            </NodeIdentifier>
                            <Address>
                                0.0.0.0
                            </Address>
                        </Creator>
                        <Delegated>
                            <NodeIdentifier>
                                Not set
                            </NodeIdentifier>
                            <Address>
                                0.0.0.0
                            </Address>
                        </Delegated>
                        <Delegatable>
                            true
                        </Delegatable>
                        <Operational>
                            Up
                        </Operational>
                        <Administrative>
                            true
                        </Administrative>
                        <CleanupTimerExp>
                            0
                        </CleanupTimerExp>
                        <DelegationTimerExp>
                            -1
                        </DelegationTimerExp>
                        <Create>
                            false
                        </Create>
                        <StateTimerExp>
                            -1
                        </StateTimerExp>
                        <LspoIsUsed>
                            true
                        </LspoIsUsed>
                        <Identifiers>
                            <IsUsed>
                                true
                            </IsUsed>
                            <Sender>
                                192.168.0.3
                            </Sender>
                            <TeLspID>
                                3
                            </TeLspID>
                            <TunnelID>
                                7008
                            </TunnelID>
                            <ExtTunnelID>
                                3232235526
                            </ExtTunnelID>
                        </Identifiers>
                        <paths>
                            <Entry>
                                <ERO>
                                    <IsUsed>
                                        true
                                    </IsUsed>
                                    <Cost>
                                        0
                                    </Cost>
                                    <Addresses>
                                        <Entry>
                                            192.168.0.5
                                        </Entry>
                                        <Entry>
                                            192.168.0.6
                                        </Entry>
                                    </Addresses>
                                    <Subobjects>
                                        <Entry>
                                            <SubobjType>
                                                1
                                            </SubobjType>
                                            <IPv4Address>
                                                192.168.0.5
                                            </IPv4Address>
                                            <IPv4PrefixLen>
                                                32
                                            </IPv4PrefixLen>
                                            <Strict>
                                                true
                                            </Strict>
                                            <Global>
                                                false
                                            </Global>
                                            <MPLSLabel>
                                                0
                                            </MPLSLabel>
                                            <SegmentIDType>
                                                UnknownSegmentID
                                            </SegmentIDType>
                                            <OnlyValidMPLSLabel>
                                                false
                                            </OnlyValidMPLSLabel>
                                            <CompleteMPLSLabelEntry>
                                                false
                                            </CompleteMPLSLabelEntry>
                                            <MissingSegmentID>
                                                false
                                            </MissingSegmentID>
                                            <MissingNodeAdjcencyID>
                                                false
                                            </MissingNodeAdjcencyID>
                                            <SegmentIDExists>
                                                false
                                            </SegmentIDExists>
                                            <SegmentIDValue>
                                                0
                                            </SegmentIDValue>
                                            <NodeAdjacencyIDExists>
                                                false
                                            </NodeAdjacencyIDExists>
                                            <NodeID>
                                                0.0.0.0
                                            </NodeID>
                                            <LocalAddress>
                                                0.0.0.0
                                            </LocalAddress>
                                            <RemoteAddress>
                                                0.0.0.0
                                            </RemoteAddress>
                                        </Entry>
                                        <Entry>
                                            <SubobjType>
                                                1
                                            </SubobjType>
                                            <IPv4Address>
                                                192.168.0.6
                                            </IPv4Address>
                                            <IPv4PrefixLen>
                                                32
                                            </IPv4PrefixLen>
                                            <Strict>
                                                true
                                            </Strict>
                                            <Global>
                                                false
                                            </Global>
                                            <MPLSLabel>
                                                0
                                            </MPLSLabel>
                                            <SegmentIDType>
                                                UnknownSegmentID
                                            </SegmentIDType>
                                            <OnlyValidMPLSLabel>
                                                false
                                            </OnlyValidMPLSLabel>
                                            <CompleteMPLSLabelEntry>
                                                false
                                            </CompleteMPLSLabelEntry>
                                            <MissingSegmentID>
                                                false
                                            </MissingSegmentID>
                                            <MissingNodeAdjcencyID>
                                                false
                                            </MissingNodeAdjcencyID>
                                            <SegmentIDExists>
                                                false
                                            </SegmentIDExists>
                                            <SegmentIDValue>
                                                0
                                            </SegmentIDValue>
                                            <NodeAdjacencyIDExists>
                                                false
                                            </NodeAdjacencyIDExists>
                                            <NodeID>
                                                0.0.0.0
                                            </NodeID>
                                            <LocalAddress>
                                                0.0.0.0
                                            </LocalAddress>
                                            <RemoteAddress>
                                                0.0.0.0
                                            </RemoteAddress>
                                        </Entry>
                                    </Subobjects>
                                </ERO>
                                <LSPA>
                                    <IsUsed>
                                        true
                                    </IsUsed>
                                    <ExludeAny>
                                        0
                                    </ExludeAny>
                                    <IncludeAny>
                                        0
                                    </IncludeAny>
                                    <IncludeAll>
                                        0
                                    </IncludeAll>
                                    <Setup>
                                        7
                                    </Setup>
                                    <Hold>
                                        7
                                    </Hold>
                                    <LBit>
                                        false
                                    </LBit>
                                </LSPA>
                                <RRO>
                                    <IsUsed>
                                        false
                                    </IsUsed>
                                    <Cost>
                                        0
                                    </Cost>
                                    <Addresses/>
                                    <Subobjects/>
                                </RRO>
                                <Bw>
                                    0
                                </Bw>
                                <isBwUsed>
                                    true
                                </isBwUsed>
                                <ReoptBw>
                                    0
                                </ReoptBw>
                                <isReoptBwUsed>
                                    false
                                </isReoptBwUsed>
                                <Metrics/>
                            </Entry>
                        </paths>
                        <ForwardClassID>
                            0
                        </ForwardClassID>
                        <LoadShare>
                            0
                        </LoadShare>
                        <Autoroute>
                            <IsUsed>
                                false
                            </IsUsed>
                            <Announced>
                                false
                            </Announced>
                            <MetricType>
                                None
                            </MetricType>
                            <Metric>
                                0
                            </Metric>
                            <Destinations/>
                        </Autoroute>
                        <BackupPath/>
                        <DelegationStatus>
                            No PCE Available
                        </DelegationStatus>
                        <PathSetupType>
                            0
                        </PathSetupType>
                        <BindingSID>
                            24013
                        </BindingSID>
                    </LSP>
                </LSPTable>
            </MPLS_PCE>
        </Operational>
    </data>
</rpc-reply>
]]>]]>'''


rsxmlstr=Get_PCEP_LSP_Result[:-6]
print rsxmlstr
print "####After cut the tail length :"+str(len(rsxmlstr))

print '#------------------Netconf XML version parsing here:---------------------------------------------'
tree=ET.fromstring(rsxmlstr)
for child in tree.iter():
    #print child.tag
    if child.tag=='{urn:ietf:params:xml:ns:netconf:base:1.0}TunnelID' :
        print "Tunnel id :"+child.text+"  Lenth:"+str(len(child.text))
        print type(child.text)
        tunnel_id=child.text[33:-29]
        print tunnel_id
        print len(child.text[33:-29])
    if child.tag=='{urn:ietf:params:xml:ns:netconf:base:1.0}SymbolicName' :
        print "Path Naming:"+child.text+"  Lenth:"+str(len(child.text))
        
print Set_route_TE%(tunnel_id)   #Netconf XML to setup static route to PCC auto tunnel id