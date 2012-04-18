import QtQuick 1.1
import com.nokia.meego 1.0
import com.nokia.extras 1.0

Window {
    id: rootWindow

    /* trigger notification
       with a given message */
    function notify(text) {
        notification.text = text;
        notification.show()
        }

    /** Grey background **/

    Rectangle {
        id : greyBackground
        color : "grey"
        anchors.fill : parent
    }

    /** Window content **/

    Flickable {
        anchors.fill : parent
        //anchors.centerIn : parent
        Column {
            spacing : 16
            Text {
                text: "PySide Example"
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Text {
                text: example.getDate()
                anchors.horizontalCenter: parent.horizontalCenter
            }
            TextField {
                anchors.horizontalCenter: parent.horizontalCenter
                id : entryField
                width : 200
                height : startButton.height
                text : "image caption"
            }
            Image {
                anchors.horizontalCenter: parent.horizontalCenter
                width : 200
                height : 200
                smooth : true
                // NOTE: the image provider name in the Image.source URL is automatically lower-cased !!
                source : "image://from_python/" + entryField.text
            }
            Button {
                anchors.horizontalCenter: parent.horizontalCenter
                width : 100
                id : startButton
                text : "notification"
                onClicked : {
                    example.notify("entry filed content:<br>" + entryField.text)
                }
            }
        }
    }

    /** Notification banner **/

    InfoBanner {
        id: notification
        timerShowTime : 5000
        height : rootWindow.height/5.0
        // prevent overlapping with status bar
        y : 8

    }
}