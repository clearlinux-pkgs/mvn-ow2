Name     : mvn-ow2
Version  : 6.1.1
Release  : 2
URL      : https://projects.ow2.org
Source0  : https://repo1.maven.org/maven2/org/ow2/ow2/1.3/ow2-1.3.pom
Source1  : https://repo1.maven.org/maven2/org/ow2/ow2/1.5/ow2-1.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1+

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/ow2/1.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/ow2/ow2/1.3

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/ow2/ow2/1.5
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/ow2/ow2/1.5


%files
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/ow2/ow2/1.3/ow2-1.3.pom
/usr/share/java/.m2/repository/org/ow2/ow2/1.5/ow2-1.5.pom
