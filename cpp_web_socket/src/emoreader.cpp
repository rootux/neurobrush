//============================================================================
// Name        : emoreader.cpp
// Author      : 
// Version     :
// Copyright   : 
// Description : a half baked work - you can hack it if you prefer c++ over java as the data_publisher
//============================================================================

#include <iostream>
#include <unistd.h>
#include <cstring>

#include "libwebsockets.h"
#include "emostate.h"

using namespace std;

struct per_session_data__http {
    emo_state *state;
};

static int callback_http(struct libwebsocket_context *context,
        struct libwebsocket *wsi,
        enum libwebsocket_callback_reasons reason, void *user,
                               void *in, size_t len)
{
    struct per_session_data__http *pss =
                (struct per_session_data__http *)user;
    switch (reason) {
        case LWS_CALLBACK_HTTP: {
            pss->state = new emo_state;
            if (pss->state->connect(true) != EDK_OK) {
               cerr << "EMotive Connection error!" << endl;
               goto handler_err;
            }

            char headers[] =
                    "HTTP/1.0 200 OK\x0d\x0a"
                    "Server: libwebsockets\x0d\x0a"
                    "Content-Type: application/json\x0d\x0a";


            if (libwebsocket_write(
                    wsi, reinterpret_cast<unsigned char *>(&headers), sizeof(headers), LWS_WRITE_HTTP) < 0) {
                cerr  <<"Write error" << endl;
                goto handler_err;
            }

            libwebsocket_callback_on_writable(context, wsi);
            break;
         }

        case LWS_CALLBACK_HTTP_FILE_COMPLETION:
            /* kill the connection after we sent one file */
            goto handler_err;

        case LWS_CALLBACK_HTTP_WRITEABLE: {
            string js = pss->state->jsonify();
            size_t len = js.length();
            // TODO: Fix strdup() memory leak
            if (libwebsocket_write(
                    wsi, reinterpret_cast<unsigned char *>(strdup(js.c_str())), len, LWS_WRITE_HTTP) < 0) {
                goto handler_err;
            }

            libwebsocket_callback_on_writable(context, wsi);
            break;
        }

        default:
            break;
    }

    return 0;

handler_err:
    delete pss->state;
    pss->state = NULL;
    return -1;
}

static struct libwebsocket_protocols protocols[] = {
    /* first protocol must always be HTTP handler */

    {
        "http-only",        /* name */
        callback_http,      /* callback */
        sizeof (struct per_session_data__http), /* per_session_data_size */
        0,          /* max frame size / rx buffer */
    },
/*    {
        "dumb-increment-protocol",
        callback_dumb_increment,
        sizeof(struct per_session_data__dumb_increment),
        10,
    },
    {
        "lws-mirror-protocol",
        callback_lws_mirror,
        sizeof(struct per_session_data__lws_mirror),
        128,
    },*/
    { NULL, NULL, 0, 0 } /* terminator */
};

libwebsocket_context * init_ws()
{
    struct lws_context_creation_info info;
    memset(&info, 0, sizeof info);
    info.port = 9000;
    info.iface = NULL;
    info.protocols = protocols;
    info.ssl_cert_filepath = NULL;
    info.ssl_private_key_filepath = NULL;
    info.gid = -1;
    info.uid = -1;
    info.options = 0;

    libwebsocket_context *const context = libwebsocket_create_context(&info);
    if (context == NULL) {
        cerr << "libwebsocket init failed" << endl;
    }

    return context;
}

static int run_service(libwebsocket_context *context)
{

    int n = 0;
    do {
        n = libwebsocket_service(context, 50);
    } while (n >= 0);

    return n;
}

int main() {
    libwebsocket_context *const context = init_ws();
    if (NULL == context) return 1;

    //emo_state state;

    run_service(context);
/*
    EmoEngineEventHandle eEvent = EE_EmoEngineEventCreate();
    EmoStateHandle eState = EE_EmoStateCreate();

    unsigned int userID = 0;
    const unsigned short composerPort = 1726;
    const bool connected = (EE_EngineConnect() == EDK_OK);//(EE_EngineRemoteConnect("127.0.0.1",composerPort)==EDK_OK);

	cout << "Connected state:" << connected << endl;
	if (connected) {
	    int lasterr = EDK_UNKNOWN_ERROR;
	    while (true) {
	        lasterr = EE_EngineGetNextEvent(eEvent);
	        switch (lasterr) {
	        case EDK_NO_EVENT:
	            sleep(1);
	            break;

	        case EDK_OK:
	            cout << "Got good event!" << endl;
	            break;

	        default:
	            goto edk_error;
	        }

	    }

	    edk_error:
	    cerr << "Got error" << lasterr << endl;

	    EE_EmoStateFree(eState);
	    EE_EmoEngineEventFree(eEvent);

	}
*/
	return 0;
}
