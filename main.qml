import QtQuick 1.1
import com.nokia.meego 1.0


Window {
    Rectangle {
        id : greyBackground
        color : "grey"
        anchors.fill : parent
    }
    Flickable {
        anchors.centerIn : parent
        Column {
            spacing : 16
            Text {
                text: "Hello World"
                anchors.horizontalCenter: parent.horizontalCenter
            }
            Text {
                text: "date"
                anchors.horizontalCenter: parent.horizontalCenter
            }

            Image {
                anchors.horizontalCenter: parent.horizontalCenter
                width : 200
                //height : 200
                source : "image://fromPython" + entryField.text
            }
            TextField {
                anchors.horizontalCenter: parent.horizontalCenter
                id : entryField
                width : 200
                height : startButton.height
                text : "write here"
            }
            Button {
                anchors.horizontalCenter: parent.horizontalCenter
                width : 100
                id : startButton
                text : "start"
            }
        }
    }
}