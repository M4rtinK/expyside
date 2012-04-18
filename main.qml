import QtQuick 1.1
import com.nokia.meego 1.0


Window {
    Rectangle {
        id : greyBackground
        color : "grey"
        anchors.fill : parent
    }
    Flickable {
        anchors.fill : parent
        //anchors.centerIn : parent
        Column {
            spacing : 16
            Text {
                text: "Hello World"
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
                //source : "pyside.svg"
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