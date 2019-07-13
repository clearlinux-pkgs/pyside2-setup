#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyside2-setup
Version  : 5.11.2
Release  : 30
URL      : http://download.qt.io/official_releases/QtForPython/pyside2/PySide2-5.11.2-src/pyside-setup-everywhere-src-5.11.2.tar.xz
Source0  : http://download.qt.io/official_releases/QtForPython/pyside2/PySide2-5.11.2-src/pyside-setup-everywhere-src-5.11.2.tar.xz
Summary  : Support library for Python bindings of Qt5-based libraries.
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: pyside2-setup-bin = %{version}-%{release}
Requires: pyside2-setup-data = %{version}-%{release}
Requires: pyside2-setup-lib = %{version}-%{release}
Requires: pyside2-setup-license = %{version}-%{release}
Requires: pyside2-setup-man = %{version}-%{release}
Requires: pyside2-setup-python = %{version}-%{release}
Requires: pyside2-setup-python3 = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-kde
BuildRequires : buildreq-qmake
BuildRequires : graphviz
BuildRequires : idna
BuildRequires : libxml2
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : numpy
BuildRequires : pyside2-setup-dev
BuildRequires : python3-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-staticdev
BuildRequires : qtwebengine-dev
Patch1: build.patch
Patch2: 0001-Dirty-fix-to-find-Clang-headers-in-Clear.patch

%description
The SameGame example can interface with a simple PHP script to store XML high score data on a remote server. We do not have a publically accessible server available for this use, but if you have access to a PHP capable webserver you can copy the files (score_data.xml, score.php, score_style.xsl) to it and alter the highscore_server variable at the top of the samegame.js file to point to it.

%package bin
Summary: bin components for the pyside2-setup package.
Group: Binaries
Requires: pyside2-setup-data = %{version}-%{release}
Requires: pyside2-setup-license = %{version}-%{release}

%description bin
bin components for the pyside2-setup package.


%package data
Summary: data components for the pyside2-setup package.
Group: Data

%description data
data components for the pyside2-setup package.


%package dev
Summary: dev components for the pyside2-setup package.
Group: Development
Requires: pyside2-setup-lib = %{version}-%{release}
Requires: pyside2-setup-bin = %{version}-%{release}
Requires: pyside2-setup-data = %{version}-%{release}
Provides: pyside2-setup-devel = %{version}-%{release}
Requires: pyside2-setup = %{version}-%{release}

%description dev
dev components for the pyside2-setup package.


%package lib
Summary: lib components for the pyside2-setup package.
Group: Libraries
Requires: pyside2-setup-data = %{version}-%{release}
Requires: pyside2-setup-license = %{version}-%{release}

%description lib
lib components for the pyside2-setup package.


%package license
Summary: license components for the pyside2-setup package.
Group: Default

%description license
license components for the pyside2-setup package.


%package man
Summary: man components for the pyside2-setup package.
Group: Default

%description man
man components for the pyside2-setup package.


%package python
Summary: python components for the pyside2-setup package.
Group: Default
Requires: pyside2-setup-python3 = %{version}-%{release}

%description python
python components for the pyside2-setup package.


%package python3
Summary: python3 components for the pyside2-setup package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pyside2-setup package.


%prep
%setup -q -n pyside-setup-everywhere-src-5.11.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561248290
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyside2-setup
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/pyside2-setup/LICENSE.FDL
cp LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/pyside2-setup/LICENSE.GPL2
cp LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/pyside2-setup/LICENSE.GPLv3
cp LICENSE.GPLv3-EXCEPT %{buildroot}/usr/share/package-licenses/pyside2-setup/LICENSE.GPLv3-EXCEPT
cp LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/pyside2-setup/LICENSE.LGPLv3
cp sources/patchelf/COPYING %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_patchelf_COPYING
cp sources/pyside2-tools/LICENSE-lupdate %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-lupdate
cp sources/pyside2-tools/LICENSE-rcc %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-rcc
cp sources/pyside2-tools/LICENSE-uic %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-uic
cp sources/pyside2/COPYING %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2_COPYING
cp sources/pyside2/PySide2/licensecomment.txt %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2_PySide2_licensecomment.txt
cp sources/pyside2/doc/codesnippets/examples/dialogs/licensewizard/licensewizard.cpp %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2_doc_codesnippets_examples_dialogs_licensewizard_licensewizard.cpp
cp sources/pyside2/doc/codesnippets/examples/dialogs/licensewizard/licensewizard.h %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_pyside2_doc_codesnippets_examples_dialogs_licensewizard_licensewizard.h
cp sources/shiboken2/ApiExtractor/COPYING %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_shiboken2_ApiExtractor_COPYING
cp sources/shiboken2/COPYING %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING
cp sources/shiboken2/COPYING.libsample %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING.libsample
cp sources/shiboken2/COPYING.libshiboken %{buildroot}/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING.libshiboken
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
stage=4
if [ $stage -gt 1 ]; then
pushd sources/shiboken2
mkdir build
pushd build
%cmake ..
make %{?_smp_mflags}
%make_install
popd
popd
if [ $stage -gt 2 ]; then
pushd sources/pyside2
mkdir build
pushd build
%cmake .. -DPYTHON_EXECUTABLE=/usr/bin/python3
make  %{?_smp_mflags}
%make_install
popd
popd
if [ $stage -gt 3 ]; then
pushd sources/pyside2-tools
mkdir build
pushd build
%cmake ..
make  %{?_smp_mflags}
%make_install
popd
popd
fi
fi
fi
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyside2-lupdate
/usr/bin/pyside2-rcc
/usr/bin/pyside2-uic
/usr/bin/shiboken2

%files data
%defattr(-,root,root,-)
/usr/share/PySide2/typesystems/typesystem_3danimation.xml
/usr/share/PySide2/typesystems/typesystem_3dcore.xml
/usr/share/PySide2/typesystems/typesystem_3dextras.xml
/usr/share/PySide2/typesystems/typesystem_3dinput.xml
/usr/share/PySide2/typesystems/typesystem_3dlogic.xml
/usr/share/PySide2/typesystems/typesystem_3drender.xml
/usr/share/PySide2/typesystems/typesystem_charts.xml
/usr/share/PySide2/typesystems/typesystem_concurrent.xml
/usr/share/PySide2/typesystems/typesystem_core.xml
/usr/share/PySide2/typesystems/typesystem_core_common.xml
/usr/share/PySide2/typesystems/typesystem_core_mac.xml
/usr/share/PySide2/typesystems/typesystem_core_win.xml
/usr/share/PySide2/typesystems/typesystem_core_x11.xml
/usr/share/PySide2/typesystems/typesystem_datavisualization.xml
/usr/share/PySide2/typesystems/typesystem_gui.xml
/usr/share/PySide2/typesystems/typesystem_gui_common.xml
/usr/share/PySide2/typesystems/typesystem_gui_mac.xml
/usr/share/PySide2/typesystems/typesystem_gui_win.xml
/usr/share/PySide2/typesystems/typesystem_gui_x11.xml
/usr/share/PySide2/typesystems/typesystem_help.xml
/usr/share/PySide2/typesystems/typesystem_location.xml
/usr/share/PySide2/typesystems/typesystem_multimedia.xml
/usr/share/PySide2/typesystems/typesystem_multimedia_common.xml
/usr/share/PySide2/typesystems/typesystem_multimedia_forward_declarations.xml
/usr/share/PySide2/typesystems/typesystem_multimediawidgets.xml
/usr/share/PySide2/typesystems/typesystem_network.xml
/usr/share/PySide2/typesystems/typesystem_opengl.xml
/usr/share/PySide2/typesystems/typesystem_positioning.xml
/usr/share/PySide2/typesystems/typesystem_printsupport.xml
/usr/share/PySide2/typesystems/typesystem_qml.xml
/usr/share/PySide2/typesystems/typesystem_quick.xml
/usr/share/PySide2/typesystems/typesystem_quickwidgets.xml
/usr/share/PySide2/typesystems/typesystem_script.xml
/usr/share/PySide2/typesystems/typesystem_scripttools.xml
/usr/share/PySide2/typesystems/typesystem_scxml.xml
/usr/share/PySide2/typesystems/typesystem_sensors.xml
/usr/share/PySide2/typesystems/typesystem_sql.xml
/usr/share/PySide2/typesystems/typesystem_svg.xml
/usr/share/PySide2/typesystems/typesystem_templates.xml
/usr/share/PySide2/typesystems/typesystem_test.xml
/usr/share/PySide2/typesystems/typesystem_texttospeech.xml
/usr/share/PySide2/typesystems/typesystem_uitools.xml
/usr/share/PySide2/typesystems/typesystem_webchannel.xml
/usr/share/PySide2/typesystems/typesystem_webengine.xml
/usr/share/PySide2/typesystems/typesystem_webenginecore.xml
/usr/share/PySide2/typesystems/typesystem_webenginewidgets.xml
/usr/share/PySide2/typesystems/typesystem_websockets.xml
/usr/share/PySide2/typesystems/typesystem_widgets.xml
/usr/share/PySide2/typesystems/typesystem_widgets_common.xml
/usr/share/PySide2/typesystems/typesystem_widgets_mac.xml
/usr/share/PySide2/typesystems/typesystem_widgets_win.xml
/usr/share/PySide2/typesystems/typesystem_widgets_x11.xml
/usr/share/PySide2/typesystems/typesystem_x11extras.xml
/usr/share/PySide2/typesystems/typesystem_xml.xml
/usr/share/PySide2/typesystems/typesystem_xmlpatterns.xml

%files dev
%defattr(-,root,root,-)
/usr/include/PySide2/Qt3DAnimation/pyside2_qt3danimation_python.h
/usr/include/PySide2/Qt3DCore/pyside2_qt3dcore_python.h
/usr/include/PySide2/Qt3DExtras/pyside2_qt3dextras_python.h
/usr/include/PySide2/Qt3DInput/pyside2_qt3dinput_python.h
/usr/include/PySide2/Qt3DLogic/pyside2_qt3dlogic_python.h
/usr/include/PySide2/Qt3DRender/pyside2_qt3drender_python.h
/usr/include/PySide2/QtCharts/pyside2_qtcharts_python.h
/usr/include/PySide2/QtConcurrent/pyside2_qtconcurrent_python.h
/usr/include/PySide2/QtCore/pyside2_qtcore_python.h
/usr/include/PySide2/QtDataVisualization/pyside2_qtdatavisualization_python.h
/usr/include/PySide2/QtGui/pyside2_qtgui_python.h
/usr/include/PySide2/QtGui/qpytextobject.h
/usr/include/PySide2/QtHelp/pyside2_qthelp_python.h
/usr/include/PySide2/QtLocation/pyside2_qtlocation_python.h
/usr/include/PySide2/QtMultimedia/pyside2_qtmultimedia_python.h
/usr/include/PySide2/QtMultimediaWidgets/pyside2_qtmultimediawidgets_python.h
/usr/include/PySide2/QtNetwork/pyside2_qtnetwork_python.h
/usr/include/PySide2/QtOpenGL/pyside2_qtopengl_python.h
/usr/include/PySide2/QtPositioning/pyside2_qtpositioning_python.h
/usr/include/PySide2/QtPrintSupport/pyside2_qtprintsupport_python.h
/usr/include/PySide2/QtQml/pyside2_qtqml_python.h
/usr/include/PySide2/QtQuick/pyside2_qtquick_python.h
/usr/include/PySide2/QtQuickWidgets/pyside2_qtquickwidgets_python.h
/usr/include/PySide2/QtScript/pyside2_qtscript_python.h
/usr/include/PySide2/QtScriptTools/pyside2_qtscripttools_python.h
/usr/include/PySide2/QtScxml/pyside2_qtscxml_python.h
/usr/include/PySide2/QtSensors/pyside2_qtsensors_python.h
/usr/include/PySide2/QtSql/pyside2_qtsql_python.h
/usr/include/PySide2/QtSvg/pyside2_qtsvg_python.h
/usr/include/PySide2/QtTest/pyside2_qttest_python.h
/usr/include/PySide2/QtTextToSpeech/pyside2_qttexttospeech_python.h
/usr/include/PySide2/QtUiTools/pyside2_qtuitools_python.h
/usr/include/PySide2/QtWebChannel/pyside2_qtwebchannel_python.h
/usr/include/PySide2/QtWebEngine/pyside2_qtwebengine_python.h
/usr/include/PySide2/QtWebEngineCore/pyside2_qtwebenginecore_python.h
/usr/include/PySide2/QtWebEngineWidgets/pyside2_qtwebenginewidgets_python.h
/usr/include/PySide2/QtWebSockets/pyside2_qtwebsockets_python.h
/usr/include/PySide2/QtWidgets/pyside2_qtwidgets_python.h
/usr/include/PySide2/QtX11Extras/pyside2_qtx11extras_python.h
/usr/include/PySide2/QtXml/pyside2_qtxml_python.h
/usr/include/PySide2/QtXmlPatterns/pyside2_qtxmlpatterns_python.h
/usr/include/PySide2/destroylistener.h
/usr/include/PySide2/dynamicqmetaobject.h
/usr/include/PySide2/globalreceiver.h
/usr/include/PySide2/pyside.h
/usr/include/PySide2/pyside2_global.h
/usr/include/PySide2/pysideclassinfo.h
/usr/include/PySide2/pysidemacros.h
/usr/include/PySide2/pysidemetafunction.h
/usr/include/PySide2/pysideproperty.h
/usr/include/PySide2/pysideqflags.h
/usr/include/PySide2/pysidesignal.h
/usr/include/PySide2/pysideweakref.h
/usr/include/PySide2/signalmanager.h
/usr/include/shiboken2/autodecref.h
/usr/include/shiboken2/basewrapper.h
/usr/include/shiboken2/bindingmanager.h
/usr/include/shiboken2/bufferprocs_py37.h
/usr/include/shiboken2/gilstate.h
/usr/include/shiboken2/helper.h
/usr/include/shiboken2/pep384impl.h
/usr/include/shiboken2/python25compat.h
/usr/include/shiboken2/qapp_macro.h
/usr/include/shiboken2/sbkarrayconverter.h
/usr/include/shiboken2/sbkconverter.h
/usr/include/shiboken2/sbkdbg.h
/usr/include/shiboken2/sbkenum.h
/usr/include/shiboken2/sbkmodule.h
/usr/include/shiboken2/sbkpython.h
/usr/include/shiboken2/sbkstring.h
/usr/include/shiboken2/sbkversion.h
/usr/include/shiboken2/shiboken.h
/usr/include/shiboken2/shibokenbuffer.h
/usr/include/shiboken2/shibokenmacros.h
/usr/include/shiboken2/signature.h
/usr/include/shiboken2/threadstatesaver.h
/usr/include/shiboken2/typespec.h
/usr/include/shiboken2/voidptr.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DAnimation/pyside2_qt3danimation_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DCore/pyside2_qt3dcore_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DExtras/pyside2_qt3dextras_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DInput/pyside2_qt3dinput_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DLogic/pyside2_qt3dlogic_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/Qt3DRender/pyside2_qt3drender_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtCharts/pyside2_qtcharts_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtConcurrent/pyside2_qtconcurrent_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtCore/pyside2_qtcore_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtDataVisualization/pyside2_qtdatavisualization_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtGui/pyside2_qtgui_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtGui/qpytextobject.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtHelp/pyside2_qthelp_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtLocation/pyside2_qtlocation_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtMultimedia/pyside2_qtmultimedia_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtMultimediaWidgets/pyside2_qtmultimediawidgets_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtNetwork/pyside2_qtnetwork_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtOpenGL/pyside2_qtopengl_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtPositioning/pyside2_qtpositioning_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtPrintSupport/pyside2_qtprintsupport_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtQml/pyside2_qtqml_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtQuick/pyside2_qtquick_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtQuickWidgets/pyside2_qtquickwidgets_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtScript/pyside2_qtscript_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtScriptTools/pyside2_qtscripttools_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtScxml/pyside2_qtscxml_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtSensors/pyside2_qtsensors_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtSql/pyside2_qtsql_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtSvg/pyside2_qtsvg_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtTest/pyside2_qttest_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtTextToSpeech/pyside2_qttexttospeech_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtUiTools/pyside2_qtuitools_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWebChannel/pyside2_qtwebchannel_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWebEngine/pyside2_qtwebengine_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWebEngineCore/pyside2_qtwebenginecore_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWebEngineWidgets/pyside2_qtwebenginewidgets_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWebSockets/pyside2_qtwebsockets_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtWidgets/pyside2_qtwidgets_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtX11Extras/pyside2_qtx11extras_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtXml/pyside2_qtxml_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/QtXmlPatterns/pyside2_qtxmlpatterns_python.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/destroylistener.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/dynamicqmetaobject.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/globalreceiver.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pyside.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pyside2_global.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysideclassinfo.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysidemacros.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysidemetafunction.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysideproperty.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysideqflags.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysidesignal.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/pysideweakref.h
/usr/lib/python3.7/site-packages/PySide2/include/PySide2/signalmanager.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/autodecref.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/basewrapper.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/bindingmanager.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/bufferprocs_py37.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/gilstate.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/helper.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/pep384impl.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/python25compat.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/qapp_macro.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkarrayconverter.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkconverter.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkdbg.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkenum.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkmodule.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkpython.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkstring.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/sbkversion.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/shiboken.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/shibokenbuffer.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/shibokenmacros.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/signature.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/threadstatesaver.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/typespec.h
/usr/lib/python3.7/site-packages/PySide2/include/shiboken2/voidptr.h
/usr/lib64/cmake/PySide2-5.11.2/PySide2Config.cmake
/usr/lib64/cmake/PySide2-5.11.2/PySide2Config.cpython-37m-x86_64-linux-gnu.cmake
/usr/lib64/cmake/PySide2-5.11.2/PySide2ConfigVersion.cmake
/usr/lib64/cmake/Shiboken2-5.11.2/Shiboken2Config.cmake
/usr/lib64/cmake/Shiboken2-5.11.2/Shiboken2Config.cpython-37m-x86_64-linux-gnu.cmake
/usr/lib64/cmake/Shiboken2-5.11.2/Shiboken2ConfigVersion.cmake
/usr/lib64/libpyside2.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/libshiboken2.cpython-37m-x86_64-linux-gnu.so
/usr/lib64/pkgconfig/pyside2.pc
/usr/lib64/pkgconfig/shiboken2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpyside2.cpython-37m-x86_64-linux-gnu.so.5.11
/usr/lib64/libpyside2.cpython-37m-x86_64-linux-gnu.so.5.11.2
/usr/lib64/libshiboken2.cpython-37m-x86_64-linux-gnu.so.5.11
/usr/lib64/libshiboken2.cpython-37m-x86_64-linux-gnu.so.5.11.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyside2-setup/LICENSE.FDL
/usr/share/package-licenses/pyside2-setup/LICENSE.GPL2
/usr/share/package-licenses/pyside2-setup/LICENSE.GPLv3
/usr/share/package-licenses/pyside2-setup/LICENSE.GPLv3-EXCEPT
/usr/share/package-licenses/pyside2-setup/LICENSE.LGPLv3
/usr/share/package-licenses/pyside2-setup/sources_patchelf_COPYING
/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-lupdate
/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-rcc
/usr/share/package-licenses/pyside2-setup/sources_pyside2-tools_LICENSE-uic
/usr/share/package-licenses/pyside2-setup/sources_pyside2_COPYING
/usr/share/package-licenses/pyside2-setup/sources_pyside2_PySide2_licensecomment.txt
/usr/share/package-licenses/pyside2-setup/sources_pyside2_doc_codesnippets_examples_dialogs_licensewizard_licensewizard.cpp
/usr/share/package-licenses/pyside2-setup/sources_pyside2_doc_codesnippets_examples_dialogs_licensewizard_licensewizard.h
/usr/share/package-licenses/pyside2-setup/sources_shiboken2_ApiExtractor_COPYING
/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING
/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING.libsample
/usr/share/package-licenses/pyside2-setup/sources_shiboken2_COPYING.libshiboken

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pyside2-lupdate.1
/usr/share/man/man1/pyside2-rcc.1
/usr/share/man/man1/pyside2-uic.1
/usr/share/man/man1/shiboken2.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
