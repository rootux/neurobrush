/*
 * emostate.cpp
 *
 *  Created on: Oct 12, 2013
 *      Author: yitzikc
 */
#include <sstream>
#include "EmoStateDLL.h"

#include "emostate.h"

using namespace std;


emo_state::emo_state() {

    m_eEvent = EE_EmoEngineEventCreate();
    m_eState = EE_EmoStateCreate();
    m_connected = false;
}

emo_state::~emo_state() {
    EE_EmoStateFree(m_eState);
    EE_EmoEngineEventFree(m_eEvent);
}

int emo_state::connect(bool use_simulator)
{
    int result = EDK_UNKNOWN_ERROR;
    if (use_simulator) {
        const unsigned short composerPort = 1726;
        result = EE_EngineRemoteConnect("127.0.0.1",composerPort);
    }
    else {
        result = EE_EngineConnect();
    }

    m_connected = (EDK_OK == result);
    return result;
}

int emo_state::update()
{
    m_percentages["WirelessSignalStatus"] = 50;
    m_percentages["ExcitementShortTerm"] = 40;
    m_percentages["ExcitementLongTerm"] = 70;
    m_percentages["EngagementBoredom"] = 50;
    m_percentages["FrustrationScore"] = 50;
    m_percentages["LowerfaceValue"] = 50;
    m_percentages["UpperfaceValue"] = 50;

    m_strs["Upperface"] = "LeftWink";
    m_strs["Lowerface"] = "RightWink";
    return EDK_OK;
}

std::string emo_state::jsonify()
{
    stringstream js;
    js << "{ ";

    for (map<string, int>::const_iterator it; it != m_percentages.end(); it++) {
        js << '"' << it->first << "\": " << it->second << ", ";
    }

    for (map<string, string>::const_iterator it; it != m_strs.end(); it++) {
        js << '"' << it->first << "\": " << it->second << ", ";
    }

    js << " }";
    return js.str();
}
