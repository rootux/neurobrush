/*
 * emostate.h
 *
 *  Created on: Oct 12, 2013
 *      Author: yitzikc
 */

#ifndef EMOSTATE_H_
#define EMOSTATE_H_

#include <map>
#include <string>

#include "edk.h"
#include "edkErrorCode.h"

class emo_state {
    std::map<std::string, int> m_percentages;
    std::map<std::string, std::string> m_strs;

    EmoEngineEventHandle m_eEvent;
    EmoStateHandle m_eState;

    bool m_connected;
public:
    emo_state();
    ~emo_state();
    std::string jsonify();

    int connect(bool use_simulator = false);
    int update();
};

#endif /* EMOSTATE_H_ */
