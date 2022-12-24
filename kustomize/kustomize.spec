%global goipath         sigs.k8s.io/kustomize
%global forgeurl        https://github.com/kubernetes-sigs/kustomize
Version: 4.5.7
%global tag             kustomize/v4.5.7

%global gomodulesmode GO111MODULE=on

%gometa

%global commit0 56d82a8378dfc8dc3b3b1085e5a6e67b82966bd7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: kustomize
Release: 1%{?dist}
Summary: Customization of kubernetes YAML configurations
License: Apache-2.0
URL: %{gourl}
Source0: %{gosource}

%description
%{summary}

%prep
%goprep -k

%build
export LDFLAGS="-X %{goipath}/api/provenance.version=%{version} \
-X %{goipath}/api/provenance.gitCommit=%{commit0} \
-X %{goipath}/api/provenance.buildDate=$(date -u -d @${SOURCE_DATE_EPOCH} +%FT%TZ) "
%gobuild -o %{gobuilddir}/bin/kustomize %{goipath}/kustomize/v4

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%files
%license LICENSE
%doc README.md OWNERS OWNERS_ALIASES code-of-conduct.md CONTRIBUTING.md ARCHITECTURE.md SECURITY_CONTACTS ROADMAP.md
%{_bindir}/*

%changelog
* Sat Dec 24 2022 Karel Van Hecke <copr@karelvanhecke.com> - 4.5.7-1
- Initial build
