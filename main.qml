import QtQuick 1.1
import com.nokia.meego 1.0
import com.nokia.extras 1.0

PageStackWindow {
    anchors.fill : parent
    id: rootWindow
    initialPage : mainPage
    showStatusBar : false
    showToolBar : true

    /* trigger notification
       with a given message */
    function notify(text) {
        notification.text = text;
        notification.show()
        }

    /** Grey background **/

    Page {
        /** Window content **/
        id : mainPage
        anchors.fill : parent
        tools : commonTools
        Flickable {
            anchors.topMargin : 16
            anchors.fill : parent
            //anchors.centerIn : parent
            Column {
                anchors.fill : parent
                spacing : 16
                Text {
                    text: "<h1>PySide & QtC @ Android Example</h1>"
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                Text {
                    text: example.getDate()
                    font.pixelSize : 32
                    anchors.horizontalCenter: parent.horizontalCenter
                }
                TextField {
                    anchors.horizontalCenter: parent.horizontalCenter
                    id : entryField
                    width : 400
                    height : 52
                    text : "image caption"
                }
                Image {
                    anchors.horizontalCenter: parent.horizontalCenter
                    width : 300
                    height : 157
                    smooth : true
                    // NOTE: the image provider name in the Image.source URL is automatically lower-cased !!
                    source : "image://from_python/" + entryField.text
                }
                Button {
                    anchors.horizontalCenter: parent.horizontalCenter
                    width : 350
                    id : startButton
                    text : "notification"
                    onClicked : {
                        example.notify("entry field content:<br><b>" + entryField.text + "</b>")
                    }
                }
            }
        }
    }


        ToolBarLayout {
            id: commonTools
            visible: true
            ToolItem { iconId: "icon-m-toolbar-back"; onClicked: pageStack.pop(); }
            ToolButton { text: "One" }
            ToolButton { text: "Two" }
            ToolIcon {
                platformIconId: "toolbar-view-menu"
                anchors.right: (parent === undefined) ? undefined : parent.right
                onClicked: (myMenu.status == DialogStatus.Closed) ? myMenu.open() : myMenu.close()
            }
        }
        Menu {
            id: myMenu
            visualParent: pageStack
            MenuLayout {
                MenuItem { text: qsTr("Sample menu item") }
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